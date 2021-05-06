from app import app
from flask import request, session, render_template, redirect, url_for, flash
from bcrypt import checkpw

from models.Usuario import Usuario


@app.route('/', methods=['GET'], endpoint='index')
def index():
    if 'logged' in session and session['logged']:
        return redirect(url_for('main'))

    else:
        return render_template('index.html')


@app.route('/main', methods=['GET'], endpoint='main')
def main():
    if 'logged' not in session or not session['logged']:
        return redirect(url_for('index'))

    else:
        return render_template('main.html')


@app.route('/login', methods=['POST'], endpoint='usuario.login')
def login():
    model = Usuario()
    usuario = model.login(request)

    senha_inserida = request.form['senha'].encode('utf8')
    senha_cadastrada = usuario.senha.encode('utf8')

    if checkpw(senha_inserida, senha_cadastrada):
        session['logged'] = True
        return redirect(url_for('main'))

    else:
        flash('Usuário ou Senha Incorreta!')
        return render_template('index.html')


@app.route('/logout', methods=['GET'], endpoint='usuario.logout')
def logout():
    session['logged'] = False
    flash('Insira o usuário e senha para continuar.')
    return redirect(url_for('index'))
