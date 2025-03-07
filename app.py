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
	create_from = forms.UserForm2(request.form)
	alumno = Alumnos.query.all()

	return render_template("index.html",form= create_from,alumnos=alumno)

@app.route("/detalles", methods=["GET","POST"])
def detalles():
	create_form=forms.UserForm2(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id = request.args.get('id')
		nombre = alum1.nombre
		apaterno = alum1.apaterno
		email = alum1.email
		return render_template("detalles.html", id=id, nombre=nombre, apaterno=apaterno, email=email)
  
@app.route("/Alumnos1",methods=['GET','POST'])
def Alumnos():
  create_from = forms.UserForm2(request.form)
  if request.method == 'POST':
   alum = Alumnos(nombre= create_from.nombre.data,
                  apaterno=create_from.apaterno.data,
                  email=create_from.email.data)
   db.session.add(alum)
   db.session.commit()
   return redirect(url_for('index'))
  return render_template('Alumnos.html',form=create_from)
if __name__ == '__main__':
	csrf.init_app(app)

	db.init_app(app)
	with app.app_context():
		db.create_all()

	app.run()