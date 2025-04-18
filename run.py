from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()


def create_app():
	app = Flask(__name__, template_folder='templates')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///./testdb.db'

	db.init_app(app)


	#impots

	migrate = Migrate(app, db)

	return app


	
