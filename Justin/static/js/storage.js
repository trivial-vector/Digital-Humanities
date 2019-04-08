// Declarations @todo move where they go
var pplDots = [];
var pplDotMap = [],
  width = 500,
  height = 1000,
  delay = 1000,
  duration = 1000,
  //story = _makeStory(),
  storyArea = d3.select('.storyArea');

//map container

function data(year) {
  d3.csv(
    'https://raw.githubusercontent.com/Wired361/Digital-Humanities/master/Data/CSV/' +
      year +
      '.csv'
  ).then(function(response) {
    let pplDots = response.map(function(d) {
      d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
      return d;
    });
    console.log(pplDots);
    return pplDots;
  });
}
d3.csv(
  'https://raw.githubusercontent.com/Wired361/Digital-Humanities/master/Data/CSV/1915.csv'
).then(function(response) {
  pplDots = response.map(function(d) {
    d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
    return d;
  });
  pplDotMap.push(pplDots);
  pplDotsOverlay.addTo(mapBox);
});

var data1900 = data('1900');
// D3 overlayLayer
var pplDotsOverlay = L.d3SvgOverlay(function(sel, proj) {
  var pplUpd = sel.selectAll('circle').data(pplDots);
  pplUpd
    .enter()
    .append('circle')
    .attr('r', (d, i) => 4)
    .attr('cx', function x(d) {
      return proj.latLngToLayerPoint(d.latLng).x;
    })
    .attr('cy', function y(d) {
      return proj.latLngToLayerPoint(d.latLng).y;
    })
    .transition(transitionDefault)
    .attr('opacity', (d, i) =>
      d['Name'].includes('NOT LISTED') || d['Name'].includes('no continuity')
        ? 0
        : 1
    )
    .attr('stroke-width', 0)
    .transition(transitionDefault)
    .delay((d, i) => (d['Name'].includes('©') ? 0 : i * 20))
    .attr('fill', (d, i) => (d['Name'].includes('©') ? 'black' : 'red'));
});
/* function _play1900(sel, proj) {
  sel
    .selectAll('circle')
    .data(data1900)
    .enter()
    .append('circle')
    .attr('r', 2)
    .attr('cx', d => proj.latLngToLayerPoint(d.latLng).x)
    .attr('cy', d => proj.latLngToLayerPoint(d.latLng).y)
    .attr('fill', 'black')
    .attr('opacity', (d, i) =>
      d['Name'].includes('NOT LISTED') || d['Name'].includes('no continuity')
        ? 0
        : 1
    );} */

//}

function _colorRace() {
  mapBox
    .selectAll('circle')
    .transition(transitionDefault)
    .attr('r', 5)
    .style('stroke', 'black')
    .style('fill', (d, i) => (d['Name'].includes('©') ? 'black' : 'red'));
}

function _play1907() {
  mapBox
    .selectAll('circle')
    .transition(transitionDefault)
    .data(data(1907))
    .exit()
    .enter()
    .append('circle')
    .attr('r', 2)
    .attr('cx', d => proj.latLngToLayerPoint(d.latLng).x)
    .attr('cy', d => proj.latLngToLayerPoint(d.latLng).y)
    .attr('fill', 'black')
    .attr('opacity', (d, i) =>
      d['Name'].includes('NOT LISTED') || d['Name'].includes('no continuity')
        ? 0
        : 1
    );
}

function _rewind1907() {
  mapBox.selectAll('circle').interrupt();

  mapBox
    .selectAll('circle')
    .data(data(1900))
    .enter()
    .append('circle')
    .attr('r', 2)
    .attr('cx', d => proj.latLngToLayerPoint(d.latLng).x)
    .attr('cy', d => proj.latLngToLayerPoint(d.latLng).y)
    .attr('fill', 'black')
    .attr('opacity', (d, i) =>
      d['Name'].includes('NOT LISTED') || d['Name'].includes('no continuity')
        ? 0
        : 1
    );
}

var transitionDefault = d3
  .transition()
  .duration(750)
  .ease(d3.easeElastic);

// maps, maps and more maps

let mapBox = L.map('map', {
  center: [29.76, -95.378],
  zoom: 18,
  scrollWheelZoom: false,
  zoomControl: false,
  attributionControl: false
});

//baseLayer

L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution: '',
    maxZoom: 18,
    id: 'outdoors-v11',
    username: 'Wired361',
    accessToken: API_KEY
  }
).addTo(mapBox);

pplDotsOverlay.addTo(mapBox);

// pull data

/* d3.csv(
  'https://raw.githubusercontent.com/Wired361/Digital-Humanities/master/Data/CSV/1917.csv'
).then(function(response) {
  var heatArray = [];
  for (var i = 0; i < response.length; i++) {
    var location = [response[i].Longitude, response[i].Latitude];
    heatArray.push([location[0], location[1]]);
  }

  heatL = L.heatLayer(heatArray, {
    radius: 25,
    blur: 35
  });
  //heatL.addTo(myMap);
}); */
//Draw the boundary lines for the Res
L.curve(
  [
    'M',
    [29.76099, -95.37625],
    'C',
    [29.7608, -95.3779],
    [29.7625, -95.3774],
    [29.7623, -95.3794],
    'Q',
    [29.76215, -95.38025],
    [29.762, -95.38027],
    'V',
    [29.75952],
    'H',
    [-95.37937],
    'V',
    [29.75872],
    'H',
    [-95.37845],
    'V',
    [29.75832],
    'H',
    [-95.37625],
    'Z'
  ],
  { color: 'blue', fill: true, animate: 2000 }
).addTo(mapBox);

console.log(pplDotMap);
// Scrollytelling

function scroll(n, offset, func1, func2) {
  return new Waypoint({
    element: document.getElementById(n),
    handler: function(direction) {
      switch (direction) {
        case 'down':
          func1();
          break;

        case 'up':
          func2();
          break;
      }
    },
    // offset starts from the top of the div

    offset: offset
  });
}
function func() {}
//new scroll('home', '100%', , func);
//new scroll('div2', '25%', _play1900, func);
//_play1900();
