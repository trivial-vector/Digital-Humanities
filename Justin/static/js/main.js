var myMap = L.map("map", {
  center: [29.758412994217334, -95.37702055828173],
  zoom: 17
});

L.tileLayer(
  "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",
  {
    attribution:
      "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }
).addTo(myMap);

d3.csv(
  "https://raw.githubusercontent.com/Wired361/Digital-Humanities/master/Data/CSV/1915.csv"
).then(function(response) {
  var heatArray = [];
  for (var i = 0; i < response.length; i++) {
    var location = [response[i].Longitude, response[i].Latitude];
    console.log(location);
    heatArray.push([location[0], location[1]]);
  }

  L.heatLayer(heatArray, {
    radius: 17,
    blur: 35
  }).addTo(myMap);
});
