from json import *
with open('/Users/francopettigrosso/Desktop/DodgeTheCrazyPlanes/data.json') as jsonfile:
    cheese = load(jsonfile)
    print(cheese['Data']['Diffculty'])
    jsonfile.close()