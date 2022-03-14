from abc import ABC, abstractmethod


class ModelService(ABC):
    """Service than provides pre-configured neural network methods."""

    @abstractmethod
    async def get_kmeans_model(self):
        """Returns the k-means implementation."""
