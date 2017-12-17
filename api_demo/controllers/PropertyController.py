
from services.interfaces.PropertyServiceInterface import PropertyServiceInterface

class PropertyController(object):

    def __init__(self,
                 propertyService: PropertyServiceInterface):
        self._propertyService = propertyService

    def show(self, property_id):
        return self._propertyService.get_property(property_id)
