var trace1 = {
  x: ['1900', '1910', '1920'], 
  y: [730, 239, 2540], 
  name: 'Black', 
  type: 'bar'
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [78, 57, 739], 
  name: 'White', 
  type: 'bar'
};


var data = [trace1, trace2];
var layout = {barmode: 'group'};

var layout = {
  title: "Population By Race for Years 1910-1920",

  xaxis: {
    title: {
      text: 'Year',
    },
  },
  yaxis: {
    title: {
      text: 'Population',
    }
  }

};

Plotly.newPlot('myDiv', data, layout, {}, {showSendToCloud:true});