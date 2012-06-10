var url = 'http://a.tiles.mapbox.com/v3/lxbarth.map-37b0is9l.jsonp';

wax.tilejson(url, function(tilejson) {
    var m = new MM.Map('map',
    new wax.mm.connector(tilejson));

    m.setCenterZoom(new MM.Location(40.753,
        -73.929),
        12);

console.log(tilejson);
    wax.mm.zoomer(m).appendTo(m.parent);
    wax.mm.interaction()
        .map(m)
        .tilejson(tilejson)
        .on(wax.tooltip().animate(true).parent(m.parent).events());
    wax.mm.legend(m, tilejson).appendTo(m.parent);
});
