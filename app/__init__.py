# pylint: skip-file
from flask import Flask
from app.config import Config
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

#import firebase_admin
#from firebase_admin import credentials

#cred = credentials.Certificate('hypechatapp.json')
#default_app = firebase_admin.initialize_app(cred)

app = Flask(__name__)
app.config.from_object(Config)
#db = SQLAlchemy(app)
api = Api(app)

from app import routes

# endpoints de prueba
api.add_resource(routes.Index, '/')
api.add_resource(routes.Android, '/android')
api.add_resource(routes.AllUsers, '/users/all')
# hasta aqui endpoints de prueba
