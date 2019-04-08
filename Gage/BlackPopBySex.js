var trace1 = {
  x: ['1900', '1910', '1920'], 
  y: [391, 140, 1220], 
  name: 'Female', 
  type: 'bar'
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [338, 98, 1318], 
  name: 'Male', 
  type: 'bar'
};


var data = [trace1, trace2];
var layout = {barmode: 'group'};

var layout = {
  title: "Black Population by Gender for Years 1910-1920",

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