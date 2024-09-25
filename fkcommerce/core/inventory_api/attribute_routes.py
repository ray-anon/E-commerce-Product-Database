from apifairy import response , body

from core.inventory_api import inventory_attribute_api_blueprint

from core.schema import AttributeSchema 

from core.models import Attribute

from core import database

attribute_schema = AttributeSchema()



@inventory_attribute_api_blueprint.route("/attribute" , methods=['POST'])
@body(attribute_schema)
@response(attribute_schema)
def attribute_insert(kwargs):
    new_attribute = Attribute(**kwargs)
    database.session.add(new_attribute)
    database.session.commit()
    return new_attribute