from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql+pymysql://build-a-blog2:MyNewPass@localhost:8889/build-a-blog2')

app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
