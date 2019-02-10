from app import app, db, models, forms
from app.controllers import usercontroller, contractcontroller, employeecontroller

@app.route('/')
def list():
    return usercontroller.list()

@app.route('/add_user', methods=['GET', 'POST'])
def post_user():
     return usercontroller.store()

@app.route('/edit/<id>', methods=['GET', 'POST'])
def update(id):
     return usercontroller.update(id)

@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    return usercontroller.destroy(id)

@app.route('/contract')
def list_contract():
    return contractcontroller.list_contract()

@app.route('/add_contract', methods=['GET', 'POST'])
def add_contract():
     return contractcontroller.store()

@app.route('/edit_contract/<id>', methods=['GET','POST'])
def edit_contract(id):
    return contractcontroller.update(id)

@app.route('/delete_contract/<id>', methods=['GET'])
def delete_contract(id):
    return contractcontroller.destroy(id)


@app.route('/employee')
def list_employee():
    return employeecontroller.list_employee()

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
     return employeecontroller.store()

@app.route('/edit_employee/<id>', methods=['GET', 'POST'])
def edit_employee(id):
     return employeecontroller.update(id)

@app.route('/delete_employee/<id>', methods=['GET'])
def delete_employee(id):
    return employeecontroller.destroy(id)