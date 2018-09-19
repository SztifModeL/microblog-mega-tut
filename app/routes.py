from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')  # --> po wejsciu na ten adres
def login():
    form = LoginForm()  # -> stworz instancje 'form' klasy 'LoginForm' z form.py ->
    return render_template('login.html', title='Sign In', form=form)  # -> wyrenderuj szablon login.html z wykorzystaniem danych z 'form'
