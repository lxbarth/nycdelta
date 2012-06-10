# OSM Building Edits in NYC

Show edits to building footprints in the NYC area.

## Update map

Requires Python 2.7 and TileMill.

*Assumes you would like to update the map to show any building footprints
changed after 2012-01-01*

1) Run

    curl http://www.overpass-api.de/api/xapi?map?bbox=-74.26,40.49,-73.7,40.92 -o nyc.osm
    python convert.py nyc.osm nycdelta/nyc.geojson 2012-01-01

2) Open TileMill project, update legend with new date and render+upload map

## Todo

- Shapefile conversion of all edited buildings would be nice
- Don't show edits outside of NYC

