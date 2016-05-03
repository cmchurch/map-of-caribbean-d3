geojsonfile = "C:/Users/Church/Desktop/MapTest/region_wb_Caribbean_subunits.json"

import json
geojson = json.loads(open(geojsonfile).read())

import itertools
from copy import deepcopy
copygeojson=deepcopy(geojson)
for i,feature in enumerate(copygeojson['features']):
    for prop in feature['properties']:
        if (prop != 'admin'):
            del geojson['features'][i]['properties'][prop]
            
with open('C:/Users/Church/Desktop/MapTest/region_wb_Caribbean_subunits_min.json', 'w') as outfile:
    json.dump(geojson, outfile)