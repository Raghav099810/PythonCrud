from fastapi import FastAPI, HTTPException, Request
from routes.student_routes import student_routes
from fastapi_pagination import add_pagination
from schemas import BaseResponse
from constants.student_constants import status as status_code
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(
    student_routes,
    prefix="/students",
    tags=["Students"]
)

add_pagination(app)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exceptions: RequestValidationError):
    errors = []
    for err in exceptions.errors():
        errors.append({
            'field': err['loc'][-1],
            'message': err['msg']
        })
    return JSONResponse(
        status_code=status_code.HTTP_400_BAD_REQUEST,
        content=BaseResponse[None](
            data=None,
            message="Validation Failed",
            statusCode=status_code.HTTP_400_BAD_REQUEST
        ).dict() | {"Errors": errors}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException):
    return JSONResponse(
        status_code=exception.status_code,
        content=BaseResponse[None](
            data=None,
            message=exception.detail,
            statusCode=exception.status_code
        ).dict()
    )
