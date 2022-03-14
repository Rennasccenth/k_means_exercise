from typing import Optional, List

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from src.container.container import Container
from src.services.interfaces.model_service import ModelService

router = APIRouter()


@inject
async def index(
        model_service: ModelService = Depends(Provide[Container.model_service]),
):
    k_means_model = await model_service.get_kmeans_model()

    return "salvasdasde"
