from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQL_ALCHEMY_DATABASE_URI')
db=SQLAlchemy(app)  
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
bcrypt=Bcrypt(app)

from blog import routes