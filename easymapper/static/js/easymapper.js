// Initialize global variables
var this_year = new Date().getFullYear();
var map;

$(document).ready(function() {
  // Load template
  area_popup_template = _.template($('#area-popup-template').html());

  // Create layer group objects
  location_layers = L.layerGroup();

  // are we on a small screen?
  small = ($(document).width() < 480)

  // Initialize our map object
  map = L.map('map', {
      scrollWheelZoom: false,
      maxZoom: 16,
      minZoom: 9,
      maxBounds: L.latLngBounds([40.5348,-89.6842],[42.9485,-86.3168])
    })
    .on('viewreset', function(e) {
      // Handle showing/hiding/adjusting layers depending on zoom level
      if(e.target._zoom > 12) {
        this.addLayer(location_layers);
        location_layers.eachLayer(function(l) {l.setRadius(8);})
      } else if(e.target._zoom == 12) {
        this.addLayer(location_layers);
        location_layers.eachLayer(function(l) {l.setRadius(4);})
      } else if(e.target._zoom > 10) {
        this.addLayer(location_layers);
        location_layers.eachLayer(function(l) {l.setRadius(2);})
      } else if(e.target._zoom > 8) {
        this.addLayer(location_layers);
        location_layers.eachLayer(function(l) {l.setRadius(1);})
      } else {
        this.removeLayer(location_layers);
      }
    })

    // set this to the lat/lng central location you want
    .setView([41.838299, -87.706953], small ? 9 : 11);

  // base tile layer
  L.tileLayer(
    'http://{s}.tribapps.com/chicago-print/{z}/{x}/{y}.png', {
      subdomains: ['maps1', 'maps2', 'maps3', 'maps4'],
      attribution: 'Map data &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 16,
      minZoom: 9
    }).addTo(map);

  // load and build and group for location points
  location_layers.style = {
    "radius": 5,
    "color": "white",
    "weight": 1,
    "fillColor": "#005696",
    "fillOpacity": 1
  };

  $.each(locations, function(i, location) {
    if(typeof(location[0]) == 'undefined')
    else
      location_layers.addLayer(
        L.circleMarker(location, location_layers.style)
      );
  });

});

