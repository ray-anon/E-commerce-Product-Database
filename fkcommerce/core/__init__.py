import os
from apifairy import APIFairy
from dotenv import load_dotenv
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


load_dotenv()

database = SQLAlchemy()

db_migration = Migrate()

ma = Marshmallow()

apifairy = APIFairy() 

def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)
    
    app.config.from_object(config_type)
    
    initalize_extensions(app)
    
    register_blueprint(app)
    
    return app

def initalize_extensions(app):
    database.init_app(app)
    
    db_migration.init_app(app , database)
    
    ma.init_app(app)
    
    apifairy.init_app(app)
    
    
    import core.models 
    
def register_blueprint(app):
    from core.inventory_api import (
        inventory_category_api_blueprint,
        inventory_product_api_blueprint,
        inventory_line_product_api_blueprint,
        inventory_product_line_image_api_blueprint,
        inventory_attribute_api_blueprint,
        inventory_seasonal_api_blueprint,
        inventory_type_api_blueprint,
        inventory_attribute_value_api_blueprint
        )
    app.register_blueprint(inventory_category_api_blueprint, url_prefix="/api")
    app.register_blueprint(inventory_product_api_blueprint , url_prefix="/api")
    app.register_blueprint(inventory_line_product_api_blueprint , url_prefix="/api")
    app.register_blueprint(inventory_product_line_image_api_blueprint , url_prefix="/api")
    app.register_blueprint(inventory_attribute_api_blueprint , url_prefix="/api")
    app.register_blueprint(inventory_seasonal_api_blueprint , url_prefix="/api")
    app.register_blueprint(inventory_type_api_blueprint , url_prefix="/api")
    app.register_blueprint(inventory_attribute_value_api_blueprint , url_prefix="/api")