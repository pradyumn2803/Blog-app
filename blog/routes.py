from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

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
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'user created successfully for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
            flash('You are logged in successfully!','success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password! Please Try Again','danger')
    return render_template("login.html",title="Login",form=form)
