from app import app, db, models, forms, router
from flask import render_template, request, redirect, url_for, flash

def list_employee():
     listEmployee= models.Employee.query.all()
     return render_template("employee/list.html", listEmployee=listEmployee)

def store():
    action = 'store'
    form = forms.EmployeeForm()
    if form.validate_on_submit():
        employee = models.Employee(
            name = form.name.data,
            phone = form.phone.data,
            email = form.email.data,
            address = form.address.data
            )
        try:
            db.session.add(employee)
            db.session.commit()
            flash('Create success', 'success')
            return redirect(url_for('list_employee'))
        except:
            flash('Error : Username already exists', 'error')
    return render_template("employee/form.html", form = form, action = action)

def update(id) :
    action = 'update'
    employee = models.Employee.query.get_or_404(id)
    form = forms.EmployeeForm(obj=employee)
    if form.validate_on_submit():
        employee.name = form.name.data
        employee.phone = form.phone.data
        employee.email = form.email.data
        employee.address = form.address.data
        try:
            db.session.commit()
            flash('Edit success', 'success')
            return redirect(url_for('list_employee'))
        except:
            flash('Error : Username already exists', 'error')
    form.name.data = employee.name
    form.email.data = employee.email
    form.phone.data = employee.phone
    form.address.data = employee.address
    return render_template('employee/form.html', form= form, action = action)

def destroy(id):
    employee = models.Employee.query.get_or_404(id)
    contract = models.Contract.query.filter_by(employee_id=id).first()
    if contract and str(contract.employee_id  == employee.id ):
        flash('Không thể xóa nhân viên ' + employee.name + ' do tồn tại hợp đồng' , 'error')
        return redirect(url_for('list_employee'))
        return render_template(title="Delete Employee")
    else:
        db.session.delete(employee)
        db.session.commit()
        flash('Delete success', 'success')
        return redirect(url_for('list_employee'))
        return render_template(title="Delete Employee")