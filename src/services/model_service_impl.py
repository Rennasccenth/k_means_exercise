from abc import ABC

from sklearn import *

from src.services.interfaces.model_service import ModelService


class ModelServiceImpl(ModelService):
    async def get_kmeans_model(self):
        pass
