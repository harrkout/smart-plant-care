from flask import Blueprint

alert = Blueprint('alert', __name__, template_folder='templates')

#from . import routes
from . import models
