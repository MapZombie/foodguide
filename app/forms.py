from flask_wtf import Form
from wtforms import StringField, RadioField, SelectField

import json
jsonFile = open('app/static/en/servings_per_day-en.json', 'r')
values = json.load(jsonFile)
from collections import OrderedDict

class UserForm(Form):
    gender=  RadioField('Gender', choices=[('male','male'),('female','female')])
    ageslist= list(OrderedDict.fromkeys([element['ages'] for element in values["servings to per to miy"]]))
    age = SelectField( label='Age', choices=[(age, age) for age in ageslist])


