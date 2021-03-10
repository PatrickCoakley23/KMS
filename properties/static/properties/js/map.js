var latitude = $('#id_latitude').text().slice(1, -1);
var lat = parseFloat(latitude);
var longitude = $('#id_longitude').text().slice(1, -1);
var lng = parseFloat(longitude);

function initMap() {

    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: {
            lat: lat,
            lng: lng
        }
    });

    var labels = "ABCDEFGHIJKLMONPQRSTUVWXYZ";

    var locations = [{
        lat: lat,
        lng: lng
    }];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, {
        imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });


}