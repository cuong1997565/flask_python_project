from app import app, db, models, forms, router
from flask import render_template, request, redirect, url_for, flash

dataStatus= [
  {
  'value': 1,
  'name' : "Tiêu chuẩn"
  },
  {
  'value': 2,
  'name' : "Chấm dứt"
  },
  {
  'value': 3,
  'name' : "Gia hạn"
  }
]
dataType = [
  {
    'value': 1,
    'name' : "Học việc"
  },
  {
    'value': 2,
    'name' : "Cộng tác viên"
  },
  {
    'value': 3,
    'name' : "Thử việc"
  },
  {
    'value': 4,
    'name' : "Thử việc"
  },
  {
    'value': 5,
    'name' : "Có thời hạn"
  },
  {
    'value': 6,
    'name' : "Không thời hạn"
  }
]
def list_contract():
    listContract= models.Contract.query.all()
    listEmployee= models.Employee.query.all()
    return render_template("contract/list.html", listContract= listContract,dataStatus = dataStatus,
    dataType=dataType,listEmployee=listEmployee)

def store():
    action = 'store'
    form = forms.ContractForm()
    if form.validate_on_submit():
        contract = models.Contract(
          title = form.title.data,
          type = form.type.data,
          status = form.status.data,
          date_sign = form.date_sign.data,
          date_effective = form.date_effective.data,
          date_expiration = form.date_expiration.data,
          employee_id = form.employee_id.data
        )
        try:
          db.session.add(contract)
          db.session.commit()
          flash('Create success', 'success')
          return redirect(url_for('list_contract'))
        except:
          flash('Error : Username already exists', 'error')
    return render_template("contract/form.html", form = form, action = action)

def update(id):
    action = 'update'
    contract = models.Contract.query.get_or_404(id)
    form = forms.ContractForm(obj=contract)
    if form.validate_on_submit():
      contract.title = form.title.data
      contract.type = form.type.data
      contract.status = form.status.data
      contract.date_sign = form.date_sign.data
      contract.date_effective = form.date_effective.data
      contract.date_expiration = form.date_expiration.data
      contract.employee_id = form.employee_id.data
      try:
        db.session.commit()
        flash('Edit success', 'success')
        return redirect(url_for('list_contract'))
      except:
        flash('Error : Employee already exists', 'error')
    form.title.data = contract.title
    form.type.data = contract.type
    form.status.data = contract.status
    form.date_sign.data = contract.date_sign
    form.date_effective.data = contract.date_effective
    form.date_expiration.data = contract.date_expiration
    return render_template("contract/form.html",form=form,action = action)

def destroy(id):
    contract = models.Contract.query.get_or_404(id)
    db.session.delete(contract)
    db.session.commit()
    flash('Delete success', 'success')
    return redirect(url_for('list_contract'))
    return render_template(title="Delete User")

