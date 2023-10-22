"""
This module handles all routes
"""
from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import RegisterForm
from app.models import User
from app.email import send_email


@app.route('/')
@app.route('/form', methods=['POST', 'GET'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
                    address=form.address.data, age=form.age.data, itIntention=form.itIntention.data,
                    expectation=form.expectation.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulation you have sucessfully registered')
        send_email('IT/Cyber Seminar',
                    sender=app.config['ADMINS'][0],
                    recipients=[user.email],
                    text_body=render_template('email.txt', firstname=user.firstname))~
        return redirect(url_for('end_page'))

    return render_template('form.html', form=form)

@app.route('/end', methods=['GET', 'POST'])
def end_page():
    return render_template('end.html')
