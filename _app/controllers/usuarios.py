from flask import render_template, request, redirect, session
from _app.models.usuario import Usuario
from _app import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/success")
def result():
    usuarios = Usuario.get_all()
    return render_template('success.html', usuarios = usuarios)

@app.route('/create_usuario', methods=["POST"])
def dojoNew():
    if not Usuario.validate_user(request.form):
        return redirect('/')
    data = {
        "correo": request.form["correo"]
    }
    email = Usuario.search_email(data)
    if not Usuario.is_exists_email(email):
        return redirect('/')
    Usuario.save(data)
    return redirect('/success')

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    Usuario.delete_user(data)
    return redirect('/success')