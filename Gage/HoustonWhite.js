var trace1 = {
  x: ['1900', '1910', '1920'], 
  y: [67, 69, 75], 
  name: 'Houston_White', 
  type: 'scatter'
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [9.65, 19.26, 22.54], 
  name: 'FreedmanTown_White', 
  type: 'scatter'
};


var data = [trace1, trace2];
var layout = {barmode: 'group'};

var layout = {
  title: "Houston Population By White Race for Years 1910-1920",

  xaxis: {
    title: {
      text: 'Year',
    },
  },
  yaxis: {
    title: {
      text: 'Percentage of Total Population',
    }
  }

};

Plotly.newPlot('myDiv', data, layout, {}, {showSendToCloud:true});