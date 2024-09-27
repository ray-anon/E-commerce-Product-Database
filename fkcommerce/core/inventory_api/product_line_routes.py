from apifairy import response , body

from core.inventory_api import inventory_line_product_api_blueprint

from core.schema import ProductLineSchema 

from core.models import ProductLine ,  AttributeValue

from core import database

product_line_schema = ProductLineSchema()



@inventory_line_product_api_blueprint.route("/product-line" , methods=['POST'])
@body(product_line_schema)
@response(product_line_schema)
def product_line_insert(kwargs):
    
    product_attributes_ids =  kwargs.pop('product_attributes_ids' , [])
    
    new_product_line = ProductLine(**kwargs)
    
    new_product_line.product_attribute = AttributeValue.query.filter(AttributeValue.id.in_(product_attributes_ids)).all()

    
    database.session.add(new_product_line)
    database.session.commit()
    return new_product_line