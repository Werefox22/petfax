from flask import Flask
app = Flask(__name__)

# Index route
@app.route('/')
def index():
	return 'Hello, and welcome to PetFax!'

# Pets index route
@app.route('/pets')
def pets():
	return 'These are our pets availible for adoption!'