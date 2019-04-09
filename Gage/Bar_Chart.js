var trace1 = {
  x: ['1900', '1910', '1920'],
  y: [193, 28, 352],
  name: 'Child(0-11)',
  type: 'bar'
};

var trace2 = {
  x: ['1900', '1910', '1920'],
  y: [137, 43, 299],
  name: '12-19',
  type: 'bar'
};

var trace3 = {
  x: ['1900', '1910', '1920'],
  y: [273, 132, 1473],
  name: '20-40',
  type: 'bar'
};

var trace4 = {
  x: ['1900', '1910', '1920'],
  y: [111, 32, 374],
  name: '40-65',
  type: 'bar'
};

var trace5 = {
  x: ['1900', '1910', '1920'],
  y: [15, 3, 40],
  name: 'Above 65',
  type: 'bar'
};

var data = [trace1, trace2, trace3, trace4, trace5];
var layout = { barmode: 'group' };

var layout = {
  title: 'Age Group of Black Population for Years 1910-1920',

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

Plotly.newPlot('myDiv', data, layout, {}, { showSendToCloud: true });
