from flask import Flask

app = Flask(__name__)

from weather_app import routes