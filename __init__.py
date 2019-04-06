"""
The flask application package.
"""

from flask import Flask
#from flask_misaka import Misaka
#from misaka import HtmlRenderer
app = Flask(__name__)
#Misaka(app, None, fenced_code=True, qoute=True)

import FlaskWebProject.views
