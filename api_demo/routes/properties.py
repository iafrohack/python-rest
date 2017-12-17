from . import routes
from containers.ControllersContainer import ControllersContainer

controllers_container = ControllersContainer()

@routes.route('/properties/<property_id>', methods=['GET'])
def show_property(property_id):
    property_controller = controllers_container.property()
    return property_controller.show(property_id)
