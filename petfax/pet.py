from flask import Blueprint, render_template
import json

pets = json.load(open("pets.json"))

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
	return render_template('index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
	if id >= 0 and id < len(pets):
		return render_template('pet_show.html', pet=pets[id])
	else:
		return '404: Sorry, that index is invalid.'

@bp.route('/new')
def new():
	return render_template('pet_new.html')