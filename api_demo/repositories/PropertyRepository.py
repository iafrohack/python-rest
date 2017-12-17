
from interface import implements
from .interfaces.PropertyRepositoryInterface import PropertyRepositoryInterface

class PropertyRepository(implements(PropertyRepositoryInterface)):

    def fetch_by_id(self, property_id):
        return "this is the propertyId we will fetch data for: " + property_id