var trace1 = {
  x: ['1900', '1910', '1920'], 
  y: [43, 6, 50], 
  name: 'Black', 
  type: 'bar'
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [6, 2, 15], 
  name: 'White', 
  type: 'bar'
};


var data = [trace1, trace2];
var layout = {barmode: 'group'};

var layout = {
  title: "Homeownership By Race for Years 1910-1920",

  xaxis: {
    title: {
      text: 'Year',
    },
  },
  yaxis: {
    title: {
      text: 'Count',
    }
  }

};

Plotly.newPlot('myDiv', data, layout, {}, {showSendToCloud:true});