from flask import Blueprint, render_template

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/')
def index():
	return "Facts index"

@bp.route('/new')
def new():
	return render_template('pet_new.html')