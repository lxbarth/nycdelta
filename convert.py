#! /usr/local/bin/python2.7

from xml.etree.ElementTree import ElementTree
from datetime import datetime
import time
from sys import argv
import json
tree = ElementTree()

if (len(argv) < 4):
    print "specify an input & output filename, and start date (YYYY-MM-DD). input is osm, output is geojson"
    exit()

tree.parse(argv[1])

fromtimestamp = time.mktime(datetime.strptime(argv[3], '%Y-%m-%d').utctimetuple())
geojson = { "type": "FeatureCollection", "features": [] }
nodeidx = {}
num = 0

print 'mapping nodes'

for n in tree.iterfind('node'):
    building = False
    for t in n.iterfind('tag'):
        if (t.get('k', '') == 'building'):
            building = True
            break

    timestamp = time.mktime(datetime.strptime(n.attrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ').utctimetuple())

    if (timestamp > fromtimestamp and building and n.attrib.has_key('user')):
        num = num + 1
        pt = {
            "type": "Feature",
            "geometry": {
                "type": 'Point',
                "coordinates": [float(n.attrib['lon']), float(n.attrib['lat'])]
            },
            "properties": {
                "user": n.attrib['user'],
                "version": n.attrib['version'],
                "timestamp": time.mktime(datetime.strptime(n.attrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ').utctimetuple()),
                "datetime": datetime.strptime(n.attrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ').strftime('%b %d %I:%M %p')
            }
        }
        geojson['features'].append(pt)

print "Converted %s nodes" % num

json.dump(geojson, open(argv[2], 'w'))
