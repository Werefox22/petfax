from flask import Flask

def create_app():
	app = Flask(__name__)

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	@app.route('/')
	def index():
		return 'Hello, PetFax!'
	
	from . import pet, facts
	app.register_blueprint(pet.bp)
	app.register_blueprint(facts.bp)

	return app