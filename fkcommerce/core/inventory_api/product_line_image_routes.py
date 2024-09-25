from apifairy import response , body

from core.inventory_api import inventory_product_line_image_api_blueprint

from core.schema import ProductLineImageSchema 

from core.models import ProductImage

from core import database

product_line_image_schema = ProductLineImageSchema()



@inventory_product_line_image_api_blueprint.route("/product-line" , methods=['POST'])
@body(product_line_image_schema)
@response(product_line_image_schema)
def product_line_insert(kwargs):
    new_product__image_line = ProductImage(**kwargs)
    database.session.add(new_product__image_line)
    database.session.commit()
    return new_product__image_line