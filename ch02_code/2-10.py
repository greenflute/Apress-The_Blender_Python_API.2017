import bpy
ut = bpy.data.texts["ut.py"].as_module()
import csv
import urllib.request

###################
# Reading in Data #
###################

# Read iris.csv from file repository
url_str = 'http://blender.chrisconlan.com/iris.csv'
iris_csv = urllib.request.urlopen(url_str)
iris_ob = csv.reader(iris_csv.read().decode('utf-8').splitlines())

# Store header as list, and data as list of lists
iris_header = []
iris_data = []

for v in iris_ob:
    if not iris_header:
        iris_header = v
    else:
        v = [float(v[0]),
             float(v[1]),
             float(v[2]),
             float(v[3]),
             str(v[4])]
        iris_data.append(v)
