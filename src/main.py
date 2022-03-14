from src.container.container import Container
from src.endpoints.default_endpoint import router

from fastapi import FastAPI


def startup_app() -> FastAPI:
    container = Container()

    fast_api = FastAPI()
    fast_api.container = container

    fast_api.router = router

    return fast_api


if __name__ == '__main__':
    app = startup_app()
    input()
