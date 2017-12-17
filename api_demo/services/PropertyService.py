
from interface import implements
from .interfaces.PropertyServiceInterface import PropertyServiceInterface
from repositories.interfaces.PropertyRepositoryInterface import PropertyRepositoryInterface

class PropertyService(implements(PropertyServiceInterface)):

    def __init__(self,
                 propertyRepository: PropertyRepositoryInterface):
        self._propertyRepository = propertyRepository

    def get_property(self, property_id):
        return self._propertyRepository.fetch_by_id(property_id)