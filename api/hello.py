# api/hello.py

from http import HTTPStatus
from typing import Any

def handler(event: Any, context: Any) -> dict:
    return {
        "statusCode": HTTPStatus.OK,
        "body": "Hello from Python!"
    }
