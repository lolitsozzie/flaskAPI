from flask import Blueprint, render_template

basicapi_bp = Blueprint('basicapi_bp', __name__)


@basicapi_bp.route('/')
def index():
    return render_template('index.html', app_name='basicAPI')