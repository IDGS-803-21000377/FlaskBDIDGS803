from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from models import db, Alumnos
from config import DevelomentConfig
import forms

app = Flask(__name__)
app.config.from_object(DevelomentConfig)
csrf = CSRFProtect(app)  


@app.route("/")
@app.route("/index")
def index():
    create_form = forms.UserForm2(request.form)
    alumnos = Alumnos.query.all()
    return render_template("index.html", form=create_form, alumnos=alumnos)

@app.route("/detalles", methods=["GET", "POST"])
def detalles():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        if id:
            try:
                id = int(id)  
                alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
                if alum1:
                    return render_template("detalles.html", id=id, nombre=alum1.nombre, apaterno=alum1.apaterno, email=alum1.email)
            except ValueError:
                pass  
    return redirect(url_for('index'))  


@app.route("/Alumnos1", methods=['GET', 'POST'])
def registrar_alumno():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST' and create_form.validate():
        nuevo_alumno = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data
        )
        db.session.add(nuevo_alumno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('Alumnos.html', form=create_form)

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()  
    app.run(debug=True)  