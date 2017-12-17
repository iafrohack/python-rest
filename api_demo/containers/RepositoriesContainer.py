
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from repositories.PropertyRepository import PropertyRepository

class RepositoriesContainer(containers.DeclarativeContainer):
    """IoC container of Repositories"""

    property = providers.Factory(PropertyRepository)
