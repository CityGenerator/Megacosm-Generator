/*
1 degree is 111km.
1 degree is 111000m.
0.01 1110m
0.00001 = 1.11m
*/
// in order to work 'Math.seed' must NOT be undefined,
// so in any case, you HAVE to provide a Math.seed
Math.seededRandom = function(max, min) {
    max = max || 1;
    min = min || 0;
    Math.seed = (Math.seed * 9301 + 49297) % 233280;
    var rnd = Math.seed / 233280;
    return min + rnd * (max - min);
}



function buildSquareHouse(x, y, length, width){
    length = length || 10; /*10 meters*/;
    width = width || 10; /*10 meters*/
    width = width*0.0000092;
    length = length*0.0000092;
    return [
               [x, y],
               [x + width, y],
               [x + width, y + length],
               [x, y + length],
           ];
}
function buildLHouse(x, y, length, width){

    length = length || 10; /*10 meters*/;
    width = width || 10; /*10 meters*/

    width = width*0.0000092;
    length = length*0.0000092;
    return [
               [x, y],
               [x + width, y],
               [x + width, y + length],
               [x + width + (width/2), y + length],
               [x + width + (width/2), y + length + (length/2)],
               [x, y + length + (length/2)],
           ];
}
/* ============================================================= */
/* ============================================================= */
/* ============================================================= */

function buildRoad(start, end, jitter){
    jitter=jitter || 0.0005;
    var road = [start];
    var delta=[  start[0]-end[0], start[1]-end[1]];
    /*console.log("start "+start);*/
    var count=60;
    jitter=jitter;
    for (i = 1 ; i <= count ; i++ ){
        var x = start[0] + -(delta[0]/count*i) + (Math.seededRandom()-.5)*jitter;
        var y = start[1] + -(delta[1]/count*i) + (Math.seededRandom()-.5)*jitter;
        road.push([x,y]);
        /*console.log("pos " + i + ": "+[x,y]);*/
    }
    console.log("end "+end);
    road.push(end);
    return road;
}

function buildRegionalRoad(ingress, egress){
    var road=[];
    var ingresspoint=[];
    var range=0.004
    switch(ingress) {
        case "North":
            ingresspoint=[range,Math.seededRandom(-range,range)]; break;
        case "South":
            ingresspoint=[-range,Math.seededRandom(-range,range)]; break;
        case "East":
            ingresspoint=[Math.seededRandom(-range,range),range]; break;
        case "West":
            ingresspoint=[Math.seededRandom(-range,range),-range]; break;
    }
    var egresspoint=[];
    switch(egress) {
        case "South":
            egresspoint=[-range,Math.seededRandom(-range,range)]; break;
        case "North":
            egresspoint=[range,Math.seededRandom(-range,range)]; break;
        case "East":
            egresspoint=[Math.seededRandom(-range,range),range]; break;
        case "West":
            egresspoint=[Math.seededRandom(-range,range),-range]; break;
    }
    var jitter=range*.02;
    var centerpoint=[ Math.seededRandom(-jitter, jitter), Math.seededRandom(-jitter, jitter)  ];
    road=buildRoad(ingresspoint,centerpoint, jitter);
    road=road.concat(buildRoad(centerpoint, egresspoint, jitter));

/*    road.push(ingresspoint);
    var count=10;
    console.log("ingress", ingresspoint[1]);
    for (i = count ; i > 0 ; i-- ){
        midpoint=ingresspoint[1]/count*i
        console.log( midpoint);
        road.push([(Math.seededRandom()-0.5)/1000 ,midpoint]);
    }

    road.push([0,0]);
    for (i = 0 ; i <=count ; i++ ){
        midpoint=egresspoint[1]/count*i
        console.log( midpoint);
        road.push([(Math.seededRandom()-0.5)/1000 ,midpoint]);
    }
    road.push(egresspoint);
*/
    return road;
}





function buildHouse(buildProperties){
    buildProperties=buildProperties||{shape:'square',lat:0, lon:0, width:4, length:8 };
    var houseparams = { stroke: true, weight:2, color: "#000", fillColor: "#666", fillOpacity: 1 };
    var house;
    switch(buildProperties['shape']){
        case 'L':
            house=L.polygon( buildLHouse(buildProperties['lat'],buildProperties['lon'],buildProperties['width'],buildProperties['length']) ,houseparams ).addTo(map);
            break;
        default:
            house=L.polygon( buildSquareHouse(buildProperties['lat'],buildProperties['lon'],buildProperties['width'],buildProperties['length']) ,houseparams ).addTo(map);
            break;
    }
    house.bindPopup(buildProperties['label']);
    var housejson=house.toGeoJSON();
    console.log(housejson);
    housejson['properties']={
              "height": 4,
            };
    var properties=buildProperties['properties']||{};
	for (var attrname in properties) { 
        housejson['properties'][attrname] = properties[attrname]; 
    }

    return housejson;
}


function extrude(buildings,properties){
    properties=properties||{};
    var geoJSON = {
      "type": "FeatureCollection",
      "features": buildings,
    }

    var osmb=new OSMBuildings(map).set(geoJSON, properties);
    osmb.date(new Date(2014, 4, 12, 4, 0));
    osmb.style({ wallColor:'rgb(100, 100, 100)', roofColor:'rgb(220, 220, 220)', shadows:true });

}

