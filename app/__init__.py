from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
# from app import forms
app = Flask(__name__)
app.config.from_object('config')
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)
# from app  import *
# from app import views
from app import models, forms ,router
