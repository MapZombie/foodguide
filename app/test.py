'''
import json
data = json.load(open('static/en/servings_per_day-en.json'))
#print(data["servings to per to miy"][0])

for criteria in values(data["servings to per to miy"]):
    for key, value in criteria.iteritems():
        print key, 'is:', value
    print ''
'''
import json
jsonFile = open('static/en/servings_per_day-en.json', 'r')
values = json.load(jsonFile)
jsonFile.close()

#for criteria in values["servings to per to miy"]:
#    for key, value in criteria.iteritems():
#        print key, 'is:', value
#    print ''

for element in values["servings to per to miy"]:
   # print(servings['servings'])
    serving_id= [element['fgid'] for element in values["servings to per to miy"]]
    print serving_id