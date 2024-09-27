from apifairy import response , body

from core.inventory_api import inventory_type_api_blueprint

from core.schema import TypeSchema 

from core.models import ProductType

from core import database

type_schema = TypeSchema()



@inventory_type_api_blueprint.route("/type" , methods=['POST'])
@body(type_schema)
@response(type_schema)
def type_insert(kwargs):
    print(kwargs)
    new_type = ProductType(**kwargs)
    database.session.add(new_type)
    database.session.commit()
    return new_type