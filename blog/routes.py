from flask import render_template, url_for, flash, redirect,request
from flask_login import login_user,current_user,logout_user,login_required
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from blog import  bcrypt,db

posts=[
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register" ,methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'user created successfully for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        login_user(user,remember=form.remember.data)
        next_page=request.args.get('next')
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            flash('You have been logged in!','success')
            return redirect(url_for('home') if not next_page else next_page)
        else:
            flash('Invalid email or password! Please Try Again','danger')
    return render_template("login.html",title="Login",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")