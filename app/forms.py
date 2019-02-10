# # from flask.ext.wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, DateField
from wtforms.validators import DataRequired
from app import models
from datetime import date


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ContractForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    status = SelectField(
        'Status',
        choices=[
        ('1', 'Tiêu chuẩn'), ('2', 'Chấm dứt'), ('3', 'Gia hạn')]
    )
    type = SelectField(
        'Type',
        choices=[
        ('1', 'Học việc'), ('2', 'Cộng tác viên'), ('3', 'Thử việc'), ('4', 'Thử việc'), ('5', 'Có thời hạn'),('6','Không thời hạn')]
    )
    date_sign = DateField('Sign Date',format='%d/%m/%Y',default=date.today())
    date_effective = DateField('Effective Date',format='%d/%m/%Y',default=date.today())
    date_expiration = DateField('Expiration Date',format='%d/%m/%Y',default=date.today())
    employee_id = SelectField(
        'Employee',
        choices=[
          (str(employee.id), employee.name)  for employee in models.Employee.query.all()
        ]
    )
    submit = SubmitField('Submit')

 # def validate_email(self, field):
 #        if models.User.query.filter_by(email=field.data).first():
 #            raise ValidationError('Email is already in use.')

 #    def validate_username(self, field):
 #        if models.User.query.filter_by(username=field.data).first():
 #            raise ValidationError('Username is already in use.')