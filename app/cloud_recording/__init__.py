from flask import Blueprint
cloud_recording = Blueprint('cloud_recording', '__init__')

from . import views  # isort:skip