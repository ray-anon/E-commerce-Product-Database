from flask import  Blueprint

inventory_category_api_blueprint = Blueprint('inventory_category_api' , __name__)
inventory_product_api_blueprint =  Blueprint('inventory_product_api' , __name__)
inventory_line_product_api_blueprint = Blueprint('inventory_line_product_api' , __name__)
inventory_product_line_image_api_blueprint = Blueprint('inventory_product_line_image_api' , __name__)
inventory_attribute_api_blueprint = Blueprint("inventory_attribute_api" , __name__)
inventory_seasonal_api_blueprint = Blueprint("inventory_seasonal_api" , __name__)
inventory_type_api_blueprint = Blueprint("inventory_type_api" , __name__)
inventory_attribute_value_api_blueprint = Blueprint("inventory_attribute_value_api" , __name__)
from . import (
    category_routes,
    product_routes,
    product_line_routes,
    product_line_image_routes,
    attribute_routes,
    seasonal_routes,
    product_type_routes,
    attribute_value_routes
    )