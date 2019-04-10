//waypoints scroll constructor
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
// Data Wrangling

let data1900 = [],
  data1907 = [],
  data1908 = [],
  data1915 = [],
  data1917 = [],
  heatData1900 = [],
  heatData1907 = [],
  heatData1908 = [],
  heatData1915 = [],
  heatData1917 = [];

dataGrab1900.map(function(d) {
  d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
  if ('Full Name' in d) {
    if (
      d['Full Name'].includes('VACANT') ||
      d['Full Name'].includes('NOT LISTED') ||
      d['Full Name'].includes('no continuity')
    ) {
    } else {
      heatData1900.push(d.latLng);
      data1900.push(d);
    }
  }
});
dataGrab1907.map(function(d) {
  d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
  if ('Full Name' in d) {
    if (
      d['Full Name'].includes('VACANT') ||
      d['Full Name'].includes('NOT LISTED') ||
      d['Full Name'].includes('no continuity')
    ) {
    } else {
      heatData1907.push(d.latLng);
      data1907.push(d);
    }
  }
});
dataGrab1908.map(function(d) {
  d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
  if ('Full Name' in d) {
    if (
      d['Full Name'].includes('VACANT') ||
      d['Full Name'].includes('NOT LISTED') ||
      d['Full Name'].includes('no continuity')
    ) {
    } else {
      heatData1908.push(d.latLng);
      data1908.push(d);
    }
  }
});
dataGrab1915.map(function(d) {
  d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
  if ('Full Name' in d) {
    if (
      d['Full Name'].includes('VACANT') ||
      d['Full Name'].includes('NOT LISTED') ||
      d['Full Name'].includes('no continuity')
    ) {
    } else {
      heatData1915.push(d.latLng);
      data1915.push(d);
    }
  }
});
dataGrab1917.map(function(d) {
  d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
  if ('Full Name' in d) {
    if (
      d['Full Name'].includes('VACANT') ||
      d['Full Name'].includes('NOT LISTED') ||
      d['Full Name'].includes('no continuity')
    ) {
    } else {
      heatData1917.push(d.latLng);
      data1917.push(d);
    }
  }
});

/* d3.json('/api/maps/1900').then(function (response) {
  response.map(function (d) {
    d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
    if ('Full Name' in d) {
      if (d['Full Name'].includes('VACANT')) {
      } else {
        heatData1900.push(d.latLng);
        data1900.push(d);
      }
    }
  });
});

d3.json('/api/maps/1907').then(function (response) {
  response.map(function (d) {
    d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
    heatData1907.push([d.Longitude, d.Latitude]);
    data1907.push(d);
  });
});

d3.json('/api/maps/1908').then(function (response) {
  response.map(function (d) {
    d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
    heatData1908.push([d.Longitude, d.Latitude]);
    data1908.push(d);
  });
});

d3.json('/api/maps/1915').then(function (response) {
  response.map(function (d) {
    d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
    heatData1915.push([d.Longitude, d.Latitude]);
    data1915.push(d);
  });
});

d3.json('/api/maps/1917').then(function (response) {
  response.map(function (d) {
    d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
    heatData1917.push([d.Longitude, d.Latitude]);
    data1917.push(d);
  });
}); */

console.log(data1900);
//baseLayers

let light = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution: '',
    maxZoom: 19,
    id: 'light-v10',
    username: 'Wired361',
    accessToken:
      'pk.eyJ1Ijoid2lyZWQzNjEiLCJhIjoiY2p0bGlteGppMGI2dzRicGthbWRjNGhhdSJ9.RopVXgG4fVgIXJ0_1FPdHQ'
  }
);
let grayscale = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution: '',
    maxZoom: 19,
    id: 'light-v10',
    username: 'Wired361',
    accessToken:
      'pk.eyJ1Ijoid2lyZWQzNjEiLCJhIjoiY2p0bGlteGppMGI2dzRicGthbWRjNGhhdSJ9.RopVXgG4fVgIXJ0_1FPdHQ'
  }
);
let streets = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution: '',
    maxZoom: 19,
    id: 'outdoors-v11',
    username: 'Wired361',
    accessToken:
      'pk.eyJ1Ijoid2lyZWQzNjEiLCJhIjoiY2p0bGlteGppMGI2dzRicGthbWRjNGhhdSJ9.RopVXgG4fVgIXJ0_1FPdHQ'
  }
);

//Res Outline
let resOutline = L.curve(
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
  { color: 'red', 'border-style': 'dotted', fill: true, animate: 2000 }
);

//D3 overlay Layers
//1900
let dots1900 = L.d3SvgOverlay(function(selection, projection) {
  var ppl1900 = selection.selectAll('circle').data(data1900);
  ppl1900
    .enter()
    .append('circle')
    .attr('r', 3)
    .attr('fill', (d, i) =>
      d['Race_Color'] == 'B' || d['Full Name'].includes('©')
        ? 'var(--prussian-blue)'
        : 'var(--red-inactive)'
    )
    .attr('cx', function x(d) {
      return projection.latLngToLayerPoint(d.latLng).x;
    })
    .attr('cy', function y(d) {
      return projection.latLngToLayerPoint(d.latLng).y;
    })
    .attr('opacity', 0.8);
});

//1907
let dots1907 = L.d3SvgOverlay(function(selection, projection) {
  var ppl1907 = selection.selectAll('circle').data(data1907);
  ppl1907
    .enter()
    .append('circle')
    .attr('r', 3)
    .attr('fill', (d, i) =>
      d['Race_Color'] == 'B' || d['Full Name'].includes('©')
        ? 'var(--prussian-blue)'
        : 'var(--red-inactive)'
    )
    .attr('cx', function x(d) {
      return projection.latLngToLayerPoint(d.latLng).x;
    })
    .attr('cy', function y(d) {
      return projection.latLngToLayerPoint(d.latLng).y;
    })
    .attr('opacity', 0.8);
});

let dots1908 = L.d3SvgOverlay(function(selection, projection) {
  var ppl1908 = selection.selectAll('circle').data(data1908);
  ppl1908
    .enter()
    .append('circle')
    .attr('r', 3)
    .attr('fill', (d, i) =>
      d['Race_Color'] == 'B' || d['Full Name'].includes('©')
        ? 'var(--prussian-blue)'
        : 'var(--red-inactive)'
    )
    .attr('cx', function x(d) {
      return projection.latLngToLayerPoint(d.latLng).x;
    })
    .attr('cy', function y(d) {
      return projection.latLngToLayerPoint(d.latLng).y;
    })
    .attr('opacity', 0.8);
});
//1915
let dots1915 = L.d3SvgOverlay(function(selection, projection) {
  var ppl1915 = selection.selectAll('circle').data(data1915);
  ppl1915
    .enter()
    .append('circle')
    .attr('r', 3)
    .attr('fill', (d, i) =>
      d['Race_Color'] == 'B' || d['Full Name'].includes('©')
        ? 'var(--prussian-blue)'
        : 'var(--red-inactive)'
    )
    .attr('cx', function x(d) {
      return projection.latLngToLayerPoint(d.latLng).x;
    })
    .attr('cy', function y(d) {
      return projection.latLngToLayerPoint(d.latLng).y;
    })
    .attr('opacity', 0.8);
});
//1917
let dots1917 = L.d3SvgOverlay(function(selection, projection) {
  var ppl1917 = selection.selectAll('circle').data(data1917);
  ppl1917
    .enter()
    .append('circle')
    .attr('r', 3)
    .attr('fill', (d, i) =>
      d['Race_Color'] == 'B' || d['Full Name'].includes('©')
        ? 'var(--prussian-blue)'
        : 'var(--red-inactive)'
    )
    .attr('cx', function x(d) {
      return projection.latLngToLayerPoint(d.latLng).x;
    })
    .attr('cy', function y(d) {
      return projection.latLngToLayerPoint(d.latLng).y;
    })
    .attr('opacity', 0.8);
});

//Heat Layers

//heatLayer 1900
let heat1900 = L.heatLayer(heatData1900, {
  radius: 20,
  blur: 35
});

let heat1907 = L.heatLayer(heatData1907, {
  radius: 20,
  blur: 35
});
let heat1908 = L.heatLayer(heatData1908, {
  radius: 20,
  blur: 35
});
let heat1915 = L.heatLayer(heatData1915, {
  radius: 20,
  blur: 35
});
let heat1917 = L.heatLayer(heatData1917, {
  radius: 20,
  blur: 35
});

//Map Set up
let karikaMap = L.map('karikaMap', {
  center: [29.76, -95.378],
  zoom: 16.3,
  layers: [grayscale, resOutline, dots1917],
  scrollWheelZoom: false,
  attributionControl: false,
  zoomControl: false
});

let resMap = L.map('map', {
  center: [29.76, -95.378],
  zoom: 17,
  layers: [light, resOutline, dots1917],
  scrollWheelZoom: false,
  attributionControl: false
});
var baseMaps = {
  Streets: streets,
  Grayscale: light
};

var overlayMaps = {
  'Reservation Outline': resOutline,
  '1900 Residents by Race': dots1900,
  '1907 Residents by Race': dots1907,
  '1908 Residents by Race': dots1908,
  '1915 Residents by Race': dots1915,
  '1917 Residents by Race': dots1917,
  '1900 Residents Heatmap': heat1900,
  '1907 Residents Heatmap': heat1907,
  '1908 Residents Heatmap': heat1908,
  '1915 Residents Heatmap': heat1915,
  '1917 Residents Heatmap': heat1917
};

L.control.layers(baseMaps, overlayMaps).addTo(resMap);

var trace1 = {
  x: ['1900', '1910', '1920'],
  y: [193, 28, 352],
  name: 'Child(0-11)',
  type: 'bar',
  marker: {
    color: '#003153',
    opacity: 0.7
  }
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [137, 43, 299],
  name: '12-19',
  type: 'bar',
  marker: {
    color: '#494949',
    opacity: 0.7
  }
};

var trace3 = {
  x: ['1900', '1910', '1920'],
  y: [273, 132, 1473],
  name: '20-40',
  type: 'bar',
  marker: {
    color: '#0072af',
    opacity: 0.7
  }
};

var trace4 = {
  x: ['1900', '1910', '1920'],
  y: [111, 32, 374],
  name: '40-65',
  type: 'bar',
  marker: {
    color: '#0e0f19',
    opacity: 0.7
  }
};

var trace5 = {
  x: ['1900', '1910', '1920'],
  y: [15, 3, 40],
  name: 'Above 65',
  type: 'bar',
  marker: {
    color: '#40E0D0',
    opacity: 0.7
  }
};

var data = [trace1, trace2, trace3, trace4, trace5];
var layout = { barmode: 'group' };

var layout = {
  title: 'Population Growth by Age 1900-1920',

  xaxis: {
    title: {
      text: 'Year'
    }
  },
  yaxis: {
    title: {
      text: 'Count'
    }
  }
};

Plotly.newPlot('plotDiv', data, layout, {}, { showSendToCloud: true });

var trace1 = {
  x: ['1900', '1910', '1920'],
  y: [391, 140, 1220],
  name: 'Female',
  type: 'bar',
  marker: {
    color: '#003153',
    opacity: 0.7
  }
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [338, 98, 1318],
  name: 'Male',
  type: 'bar',
  marker: {
    color: '#0072af',
    opacity: 0.7
  }
};

var data = [trace1, trace2];
var layout = { barmode: 'group' };

var layout = {
  title: 'Population Growth by Gender 1900-1920',

  xaxis: {
    title: {
      text: 'Year'
    }
  },
  yaxis: {
    title: {
      text: 'Count'
    }
  }
};

Plotly.newPlot('plotDiv2', data, layout, {}, { showSendToCloud: true });

var trace1 = {
  x: ['1900', '1910', '1920'],
  y: [32.7, 30.37, 24.6],
  name: 'Houston Black Population',
  type: 'scatter',
  marker: {
    color: '#003153',
    opacity: 0.7
  }
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [90.35, 80.74, 77.46],
  name: 'Freedmantown Black Population',
  type: 'scatter',
  marker: {
    color: '#0072af',
    opacity: 0.7
  }
};

var trace3 = {
  x: ['1900', '1910', '1920'],
  y: [67, 69, 75],
  name: 'Houston_White',
  type: 'scatter',
  marker: {
    color: '#850000',
    opacity: 0.7
  }
};

var trace4 = {
  x: ['1900', '1910', '1920'],
  y: [9.65, 19.26, 22.54],
  name: 'FreedmanTown_White',
  type: 'scatter',
  marker: {
    color: '#eb5656',
    opacity: 0.7
  }
};

var data = [trace1, trace2, trace3, trace4];

var layout = {
  title: 'Population Growth in Houston 1900-1920',

  xaxis: {
    title: {
      text: 'Year'
    }
  },
  yaxis: {
    title: {
      text: 'Percentage of Total Population'
    }
  }
};

Plotly.newPlot('plotDiv3', data, layout, { showSendToCloud: true });
