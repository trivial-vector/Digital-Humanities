var trace1 = {
  x: ['1900', '1910', '1920'], 
  y: [32.7, 30.37, 24.6], 
  name: 'Houston_Black', 
  type: 'scatter'
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [90.35, 80.74, 77.46], 
  name: 'FreedmanTown_Black', 
  type: 'scatter'
};


var data = [trace1, trace2];
var layout = {barmode: 'group'};

var layout = {
  title: "Houston Population By Black Race for Years 1910-1920",

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