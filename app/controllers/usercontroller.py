from app import app, db, models, forms, router
from flask import render_template, request, redirect, url_for, flash

def list():
    listUser = models.User.query.all()
    return render_template("user/list_user.html", listUser = listUser)

def store():
    action = 'store'
    form = forms.UserForm()

    if form.validate_on_submit():
        user = models.User(
            username = form.username.data,
            email = form.email.data
            )
        try:
            db.session.add(user)
            db.session.commit()
            flash('Create success', 'success')
            return redirect(url_for('list'))
        except:
            flash('Error : Username already exists', 'error')
    return render_template("user/add_user.html", form = form, action = action)

def update(id) :
    action = 'update'
    user = models.User.query.get_or_404(id)
    form = forms.UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        try:
            db.session.commit()
            flash('Edit success', 'success')
            return redirect(url_for('list'))
        except:
            flash('Error : Username already exists', 'error')
    form.username.data = user.username
    form.email.data = user.email
    return render_template('user/add_user.html', form= form, action = action)

def destroy(id):
    user = models.User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Delete success', 'success')
    return redirect(url_for('list'))
    return render_template(title="Delete User")