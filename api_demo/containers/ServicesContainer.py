
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from services.PropertyService import PropertyService

from .RepositoriesContainer import RepositoriesContainer

repositories_container = RepositoriesContainer()

class ServicesContainer(containers.DeclarativeContainer):
    """IoC container of Service."""

    property = providers.Factory(PropertyService,
                                 repositories_container.property()
                                 )
