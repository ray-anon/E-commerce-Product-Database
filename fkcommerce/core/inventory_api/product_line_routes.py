from apifairy import response , body

from core.inventory_api import inventory_line_product_api_blueprint

from core.schema import ProductLineSchema 

from core.models import ProductLine

from core import database

product_line_schema = ProductLineSchema()



@inventory_line_product_api_blueprint.route("/product-image-line" , methods=['POST'])
@body(product_line_schema)
@response(product_line_schema)
def product_line_image_insert(kwargs):
    new_product_line = ProductLine(**kwargs)
    database.session.add(new_product_line)
    database.session.commit()
    return new_product_line