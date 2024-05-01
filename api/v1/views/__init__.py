#!/usr/bin/python3
""" importing Blueprint create flask app 
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.vi.views.index import * 


