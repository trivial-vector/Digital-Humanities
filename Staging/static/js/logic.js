// maps, maps and more maps

var heatL;
var pplDots = [];
let map = () => {
  let myMap = L.map("map", {
    center: [29.7597, -95.378],
    zoom: 17,
    scrollWheelZoom: false,
    zoomControl: false,
    attributionControl: false
  });

  var pplDotsOverlay = L.d3SvgOverlay(function(sel, proj) {
    var pplUpd = sel.selectAll("circle").data(pplDots);
    pplUpd
      .enter()
      .append("circle")
      .attr("r", 2.5)
      .attr("cx", function(d) {
        console.log(d);
        return proj.latLngToLayerPoint(d.latLng).x;
      })
      .attr("cy", function(d) {
        return proj.latLngToLayerPoint(d.latLng).y;
      })
      .attr("stroke", "black")
      .attr("stroke-width", 1)
      .attr("fill", "gray");
  });

  L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
    {
      attribution: "",
      maxZoom: 18,
      id: "outdoors-v11",
      username: "Wired361",
      accessToken: API_KEY
    }
  ).addTo(myMap);

  d3.csv(
    "https://raw.githubusercontent.com/Wired361/Digital-Humanities/master/Data/CSV/1915.csv",
    function(response) {
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
      pplDots = response.map(function(d) {
        d.latLng = [parseFloat(d.Longitude), parseFloat(d.Latitude)];
        return d;
      });
      pplDotsOverlay.addTo(myMap);
    }
  );

  L.curve(
    [
      "M",
      [29.76099, -95.37625],
      "C",
      [29.7608, -95.3779],
      [29.7625, -95.3774],
      [29.7623, -95.3794],
      "Q",
      [29.76215, -95.38025],
      [29.762, -95.38027],
      "V",
      [29.75952],
      "H",
      [-95.37937],
      "V",
      [29.75872],
      "H",
      [-95.37845],
      "V",
      [29.75832],
      "H",
      [-95.37625],
      "Z"
    ],
    { color: "blue", fill: true, animate: 2000 }
  ).addTo(myMap);
};

let heatMapLayer = d3.select(".leaflet-heatmap-layer").attr("opacity", 0);

// Scrollytelling

//svg
let svg = d3.select("svg");

//svg width and height
svg.attr("width", 500).attr("height", 1000);

//set up grid spacing
let spacing = 40;
let rows = 15;
let column = 10;
let randnum = (min, max) => Math.round(Math.random() * (max - min) + min);

//create an array of objects simulating data
let ourData = d3.range(25).map(i => ({
  race: i < 17 ? "Black" : "White",
  age: randnum(1, 65)
}));

//create group and join our data to that group
let group1 = svg
  .selectAll("g")
  .data(ourData)
  .enter()
  .append("g");

//create rectangles
let rects = group1.append("rect");

//race data
d3.selectAll("g")
  .append("text")
  .text(d => d["race"])
  .attr("fill", "var(--prussian-blue)")
  .attr("class", "race")
  .attr("dx", -500);

//age data
d3.selectAll("g")
  .append("text")
  .text(d => d["age"])
  .attr("fill", "#fff")
  .attr("class", "age")
  .attr("dx", -500);

// square grid
let grid = () => {
  rects
    .transition()
    .delay((d, i) => 10 * i)
    .duration(600)
    .ease("elastic")
    .attr("width", 20)
    .attr("height", 20)
    .attr("rx", 5)
    .attr("ry", 5)
    .attr("x", (d, i) => (i % column) * spacing)
    .attr("y", (d, i) => (Math.floor(i / 10) % rows) * spacing)
    .attr("fill", (d, i) =>
      i < 50 ? "var(--prussian-blue)" : "var(--outer-space)"
    )
    .attr("opacity", "1");
};

//circle grid
let grid2 = () => {
  rects
    .transition()
    .delay((d, i) => 10 * i)
    .duration(600)
    .ease("elastic")
    .attr("width", 20)
    .attr("height", 20)
    .attr("rx", "50%")
    .attr("ry", "50%")
    //.attr("x", (d, i) => (i % column) * spacing)
    //.attr("y", (d, i) => (Math.floor(i / 10) % rows) * spacing)
    .attr("fill", (d, i) =>
      d["race"] == "Black" ? "var(--prussian-blue)" : "var(--outer-space)"
    );
};

//divide
let divide = () => {
  rects
    .transition()
    .delay((d, i) => 10 * i)
    .duration(600)
    .ease("elastic")
    .attr("width", 10)
    .attr("height", 10)
    .attr("rx", 0)
    .attr("ry", 0)
    .attr("x", (d, i) =>
      d["race"] == "Black" ? randnum(100, 150) : randnum(300, 350)
    )
    .attr("y", (d, i) => i * 20)
    .attr("fill", (d, i) =>
      d["race"] == "Black" ? "var(--prussian-blue)" : "var(--outer-space)"
    );

  //age
  d3.selectAll("text.age")
    .transition()
    .delay((d, i) => 40 * i)
    .duration(900)
    .ease("elastic")
    .attr("dx", -500);

  //race
  d3.selectAll("text.race")
    .transition()
    .delay((d, i) => 40 * i)
    .duration(900)
    .ease("elastic")
    .attr("dx", -500);
};

//bar cart
let barChart = () => {
  rects
    .attr("rx", 0)
    .attr("ry", 0)
    .transition()
    .delay((d, i) => 20 * i)
    .duration(900)
    .ease("elastic") //linear, quad, cubic, sin, exp, circle, elastic, back, bounce
    .attr("x", (d, i) => 150)
    .attr("y", (d, i) => i * 17)
    .attr("width", (d, i) => d["age"] * 2)
    .attr("height", (d, i) => 15)
    .attr("fill", (d, i) =>
      i < 17 ? "var(--prussian-blue)" : "var(--outer-space)"
    )
    .attr("opacity", 1)
    .attr("transform", "translate(0,0) rotate(0)")
    .attr("opacity", (d, i) => (i < 25 ? 1 : 0)); //only show 5 for now

  //age text
  d3.selectAll("text.age")
    .transition()
    .delay((d, i) => 20 * i)
    .duration(900)
    .ease("elastic")
    //align text right
    .attr("text-anchor", "start")
    .attr("dx", 160)
    .attr("dy", (d, i) => i * 17 + 12)
    .attr("opacity", (d, i) => (i < 25 ? 1 : 0)); //only show 5 ages

  //race text
  d3.selectAll("text.race")
    .transition()
    .delay((d, i) => 20 * i)
    .duration(900)
    .ease("elastic")
    //align text left
    .attr("text-anchor", "end")
    .attr("dx", 140)
    .attr("dy", (d, i) => i * 17 + 12)
    .attr("opacity", (d, i) => (i < 25 ? 1 : 0)); //only show 5 races
};

//waypoints scroll constructor
function scroll(n, offset, func1, func2) {
  return new Waypoint({
    element: document.getElementById(n),
    handler: function(direction) {
      switch (direction) {
        case "down":
          func1();
          break;

        case "up":
          func2();
          break;
      }
    },
    // offset starts from the top of the div

    offset: offset
  });
}
let func = () => {
  rects
    .transition()
    .delay(100)
    .duration(100)
    .attr("opacity", 0);
};
let heatFade = () => {
  heatMapLayer
    .transition()
    .delay(500)
    .duration(250)
    .attr("opacity", 1);
};

//triger these functions on page scroll
new scroll("home", "100%", func, func);
new scroll("map", "100%", heatFade, func);
new scroll("div1", "10%", grid, func);
new scroll("div2", "25%", grid2, grid);
new scroll("div4", "25%", divide, grid);
new scroll("div6", "25%", barChart, divide);

//start grid on page load
map();
