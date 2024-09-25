from apifairy import response , body

from core.inventory_api import inventory_product_api_blueprint

from core.schema import ProductSchema 

from core.models import Product

from core import database

product_schema = ProductSchema()



@inventory_product_api_blueprint.route("/product" , methods=['POST'])
@body(product_schema)
@response(product_schema)
def product_insert(kwargs):
    new_product = Product(**kwargs)
    database.session.add(new_product)
    database.session.commit()
    return new_product