"""Containers module."""

from dependency_injector import containers, providers


from src.services.interfaces import *


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[])

    # config = providers.Configuration(yaml_files=["config.yml"])

    model_service = providers.Factory(
        model_service.ModelService,
    )
