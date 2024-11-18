from dotenv import load_dotenv
import os

# Environment config
load_dotenv()
env = {
    'MONGODB_USER': os.getenv('MONGODB_USER'),
    'MONGODB_PASSWORD': os.getenv('MONGODB_PASSWORD'),
    'MONGODB_DATABASE': os.getenv('MONGODB_DATABASE'),
    'FLASK_ENV': os.getenv('FLASK_ENV'),
}

class Config(object):
    TESTING = False

class LocalConfig(Config):
    DB_URI = 'mongodb://localhost:27017'

class DevelopmentConfig(Config):
    DB_URI = 'mongodb://mongodb:27017'

class ProductionConfig(Config):
    DB_URI = f'mongodb+srv://{env['MONGODB_USER']}:{env['MONGODB_PASSWORD']}@cluster0.3l6s1.mongodb.net/?retryWrites=true&w=majority'

config_map = {
    'local':       LocalConfig, 
    'development': DevelopmentConfig,
    'production':  ProductionConfig
}

flask_env = env['FLASK_ENV'].lower()
config_obj = config_map[flask_env]
