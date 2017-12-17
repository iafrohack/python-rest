


import dependency_injector.containers as containers
import dependency_injector.providers as providers


from .ServicesContainer import ServicesContainer
from controllers.PropertyController import PropertyController

services_container = ServicesContainer()

class ControllersContainer(containers.DeclarativeContainer):
    """IoC container of Controllers """

    property = providers.Factory(PropertyController,
                                 services_container.property())
