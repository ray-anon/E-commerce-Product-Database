import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()


database = SQLAlchemy()

db_migration = Migrate()

def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)
    
    app.config.from_object(config_type)
    
    initalize_extensions(app)
    return app

def initalize_extensions(app):
    database.init_app(app)
    
    db_migration.init_app(app , database)
    
    import core.models 