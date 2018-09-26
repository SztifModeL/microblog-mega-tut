from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home Page', posts=posts)

@app.route('/login', methods=['GET', 'POST'])  # --> po wejsciu na /login uruchom i dodatkowo akceptuj GET i POST a nie tylko domyslne GET
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()  # -> stworz instancje 'form' klasy 'LoginForm' z forms.py ->
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()  # Szukam uzytkownika w DB -> Wynikiem filter_by() jest zapytanie zawierajace tylko obiekty o pasujacej nazwie uzytkownika. Poniewaz wiem, ze bedzie tylko jeden lub zero wynikow, wypelniam zapytanie przez wywolanie first(), ktore zwroci obiekt uzytkownika, jesli istnieje, lub None jesli nie. The first() Metoda jest innym powszechnie uzywanym sposobem wykonania zapytania, gdy potrzebujesz tylko jednego wyniku, cos jak all()
        if user is None or not user.check_password(form.password.data):  # gdy nie ma takiego usera lub password jest nie poprawny
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')  # Przechwycenie argumentu next strony z jakiej chcial skozystac niezalogowany user
        if not next_page or url_parse(next_page).netloc != '':  # if nie istnieje next_page lub analizujac next_page za pomoca url_parse() i sprawdzajac czy netloc jest ustawiony wykazala ze cos bylo wstawione (dzieki netloc moznabylo zaszyc jakis adres/przekirowanie (hacker/security))
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)  # -> wyrenderuj szablon login.html z wykorzystaniem danych z 'form'

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))