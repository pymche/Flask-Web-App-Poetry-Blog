from script import db, bcrypt
from script.models import User
from flask import render_template, url_for, flash, redirect, request, Blueprint
from script.users.forms import LoginForm, RegisterForm
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', __name__)

# Register
@users.route('/boomboomba', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():

        # Hash password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Add user info into database
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

# Login
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Check entered data form.email.data against database using query
        user = User.query.filter_by(email=form.email.data).first()

        # if user exists and password matches database
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # log in
            login_user(user)
            # if previous page exists that redirects user to log in page
            # redirect user back to that page
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))

            flash('You are now logged in', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

# Logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
    # we already know which user it is return redirect(url_for('home'))