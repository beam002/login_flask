from models import db, Members, Books
from flask import Flask, request, render_template, session, redirect, flash
from flask_migrate import Migrate
import config

migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def home():
    if session.get('logged_in'):
        return render_template('main.html')
    else:
        return render_template('signup.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get['name']
        email = request.form.get['email']
        password = request.form.get['password']
        passwordCheck = request.form.get['passwordCheck']
        user = Members.query.filter_by(email=email).first()
        if user:
            flash('이미 존재하는 유저입니다.')
            return render_template('signup.html')

        if password != passwordCheck:
            flash('패스워드 불일치')
            return render_template('signup.html')

        new_user = Members(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        session['logged_in'] = True
        return redirect('/home')

    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def log_out():
    session['logged_in'] = False
    return redirect('/log-in')


if __name__ == "__main__":
    app.run()
