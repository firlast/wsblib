from datetime import datetime

from http_pyparser import Response
from .request import RequestData


def log_request(response: Response, request: RequestData) -> None:
    time = datetime.now()

    status = response.status
    path = request.path
    method = request.method
    host = request.remote_addr[0]
