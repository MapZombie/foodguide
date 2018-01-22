from flask import Flask, request, render_template, redirect, session
application = Flask(__name__)
from app.forms import UserForm
import json, random
from collections import OrderedDict

# Main page asks for user input - age range and gender #
@application.route('/',methods=['GET','POST'])
def main():
    form = UserForm(request.form)
    if request.method == 'POST':
        session['agedata']=form.age.data
        session['genderdata']=form.gender.data

        return redirect('/mealplan')
    return render_template('index.html', form=form)

# Meal plan page #
@application.route('/mealplan', methods=['GET','POST'])
def mealplan():
    form = UserForm(request.form)
    # Get user inputs
    agedata=(session.get('agedata'))
    genderdata=(session.get('genderdata')).title()
    # Open JSON files with data
    servings = json.load(open('app/static/en/servings_per_day-en.json', 'r'))
    foods = json.load(open('app/static/en/foods-en.json', 'r'))
    # Determine number of servings by food group
    for i in servings["servings to per to miy"]:
            if i['gender'] == genderdata and i['ages'] == agedata:
                if i['fgid'] == 'vf':
                        vf =  i['servings']
                if i['fgid'] == 'gr':
                        gr =  i['servings']
                if i['fgid'] == 'mi':
                        mi =  i['servings']
                if i['fgid'] == 'me':
                        me =  i['servings']
    # Use minimum number of servings if there is a range
    vfnum=int(vf[0:1])
    grnum=int(gr[0:1])
    minum=int(mi[0:1])
    menum=int(me[0:1])
    vflist=[]
    grlist=[]
    milist=[]
    melist=[]
    # Pull foods from food list by food group
    for element in foods["foods"]:
        if element['fgid'] == 'vf':
            vflist=([element['food'] + " " + element['srvg_sz'] for element in foods["foods"] if element['fgid']=='vf' ])
        if element['fgid'] == 'gr':
            grlist=([element['food'] + " " + element['srvg_sz']for element in foods["foods"] if element['fgid']=='gr' ])
        if element['fgid'] == 'da':
            milist=([element['food'] + " " +  element['srvg_sz'] for element in foods["foods"] if element['fgid']=='da' ])
        if element['fgid'] == 'me':
            melist=([element['food'] + " " +  element['srvg_sz'] for element in foods["foods"] if element['fgid']=='me' ])

    # Randomly shuffle the lists
    def shuffle(lists):
        return random.shuffle(lists)
    shuffle(vflist)
    shuffle(grlist)
    shuffle(milist)
    shuffle(melist)
    # encode each food item utf8 to allow for better formatting in HTML
    vffoods=[x.encode('utf-8') for x in (vflist[0:vfnum])]
    grfoods=[x.encode('utf-8') for x in (grlist[0:grnum])]
    mifoods=[x.encode('utf-8') for x in (milist[0:minum])]
    mefoods=[x.encode('utf-8') for x in (melist[0:menum])]

    return render_template('mealplan.html',vfnum=vfnum, grnum=grnum, minum=minum, menum=menum, vffoods=vffoods,
grfoods=grfoods, mifoods=mifoods,mefoods=mefoods)
