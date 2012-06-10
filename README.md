# OpenStreetMap: Changes to building footprints in New York City area

[View map](http://lxbarth.github.com/nycdelta/)

This map showcases how municipal GIS departments could leverage OpenStreetMap for more efficient change management.

The particular example shows changes to New York City building footprint data between January 1st 2012
and June 6th, 2012. It is really simple though to modify convert.py to the feature type or time period
you are interested in.

Thanks to [Tom](http://mapbox.com/team/tom-macwright/) for providing [a great headstart](http://mapbox.com/blog/how-to-map-contributions-openstreetmap/).

## Update map

Requires [Python 2.7](http://www.python.org/getit/releases/2.7/) and [TileMill](http://mapbox.com/tilemill/).

*Assumes you would like to update the map to show any building footprints
changed after 2012-01-01 in NYC area*

1) Run

    curl http://www.overpass-api.de/api/xapi?map?bbox=-74.26,40.49,-73.7,40.92 -o nyc.osm
    python convert.py nyc.osm nycdelta/nyc.geojson 2012-01-01

2) Open TileMill project, update legend with new date and render+upload map

## Todo

- Pass in feature types as argument to convert.py
- Shapefile conversion of all edited buildings
- Don't show edits outside of NYC
- Clean up style.css

## Background

- This is a submission to [#PDFApplied](http://pdfapplied.challengepost.com/submissions/8241-openstreetmap-change-tracker)
- [Inspired by NYC Doitt's awesome building perimeter data ](https://skitch.com/alexbarth/895nh/quantum-gis-1.7.4-wroclaw)

