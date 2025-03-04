from flask import Flask, render_template,request,redirect,url_for
from flask import Flask
from  flask_wtf.csrf import CSRFProtect
from flask import g
import forms
from models import db
from models import Alumnos
from config import DevelomentConfig

app = Flask(__name__)
app.config.from_object(DevelomentConfig)
csrf = CSRFProtect()


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	csrf.init_app(app)

	db.init_app(app)
	with app.app_context():
		db.create_all()

	app.run()