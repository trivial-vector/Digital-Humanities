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
    color: '#494949',
    opacity: 0.7
  }
};

var trace3 = {
  x: ['1900', '1910', '1920'],
  y: [67, 69, 75],
  name: 'Houston_White',
  type: 'scatter',
  marker: {
    color: '#0072af',
    opacity: 0.7
  }
};

var trace4 = {
  x: ['1900', '1910', '1920'],
  y: [9.65, 19.26, 22.54],
  name: 'FreedmanTown_White',
  type: 'scatter',
  marker: {
    color: '#0e0f19',
    opacity: 0.7
  }
};

var data = [trace1, trace2, trace3, trace4];
var layout = { barmode: 'group' };

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

Plotly.newPlot('plotDiv3', data, layout, {}, { showSendToCloud: true });

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
