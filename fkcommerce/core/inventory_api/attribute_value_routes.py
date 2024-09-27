from apifairy import response , body

from core.inventory_api import inventory_attribute_value_api_blueprint

from core.schema import AttributeValueSchema 

from core.models import AttributeValue

from core import database

attribute_value_schema = AttributeValueSchema()



@inventory_attribute_value_api_blueprint.route("/attribute-value" , methods=['POST'])
@body(attribute_value_schema)
@response(attribute_value_schema)
def attribute_value_insert(kwargs):
    print(kwargs)
    new_attribute_value = AttributeValue(**kwargs)
    database.session.add(new_attribute_value)
    database.session.commit()
    return new_attribute_value