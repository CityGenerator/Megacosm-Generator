//
// A simple check to make sure we're not wasting everyone's time
//
if ( ! Detector.webgl ) {
    Detector.addGetWebGLMessage();
    document.getElementById( 'mapcontainer' ).innerHTML = "Sorry, you need WebGL enabled to see this.";
}


// Lets set a couple of terrain transition colors and ranges
// tcolors represent transition color points; There are doubles on the end to represent both "expected" extremes and unexpected extremes.
// this allows us to have a proper transition between snow and lightrock, yet account for elevations beyond what we'd expect for snow.
var tcolors=[

                //  snow                snow            lightrock           rock            pine            hightree        deciduous       marsh           grass 
                    [255,255,226],      [255,255,226],  [241, 213, 192],    [118, 87, 33],  [115, 145, 93], [71, 99, 2],    [39, 120, 15],  [0, 102, 51],   [75, 107, 70], 
                // pink sand            brown sand      oceanspray          shallow water   mid water       deep water      deepwater
                    [229, 207, 185],    [112, 102, 79], [136, 181, 190],    [30, 67, 81],   [0, 42, 81],    [0, 0, 81],     [0, 0, 81] 
            ]
// atp = Altitude Transition Points, in Decameters
// These are the points where transition colors lay; the actual pixel color is determined by comparing elevation to its surrounding
// transition points, then using that to find a color between the two transition color surrounding it. This gives us a nice segmented gradient.
// Note the extreme on both ends protects us from "absurd" values falling outside of a regular transition.
var atp=[
                //  snow                snow            lightrock           rock            pine            hightree        deciduous       marsh           grass 
                    100000,             550,            400,                300,            250,            100,            60,             10,             1,
                //  pink sand           brown sand      oceanspray          shallow water   mid water       deep water      deepwater
                    0.5,                0,              -.5,                -1,             -15,            -100,           -100000
        ]


// boring resize function
function onWindowResize() {
    var mapcontainer=document.getElementById( 'mapcontainer' )
    camera.aspect = mapcontainer.offsetWidth / mapcontainer.offsetHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( mapcontainer.offsetWidth, mapcontainer.offsetHeight );
}

// boring animate
function animate() {
    requestAnimationFrame( animate );
    render();
}

// Configure the renderer for the container
function setup_renderer(mapcontainer){
    renderer = new THREE.WebGLRenderer({antialias: true });
    renderer.setClearColor( 0xbfd1e5 );
    renderer.setSize(  mapcontainer.offsetWidth, mapcontainer.offsetHeight );
    renderer.shadowMapEnabled = true;
    renderer.shadowMapType = THREE.PCFSoftShadowMap;
    mapcontainer.appendChild( renderer.domElement );
}

// boring render
function render() {
    controls.update( clock.getDelta() );
    renderer.render( scene, camera );
}

function generateBaseElevation(){
    // FIXME this is a sloppy way to skew elevation to be low...
    var elevationrandom =1.1*Math.sin(1.5*(Math.random())-1.6)+1.1;

    // Starting elevation, between 0 and 360 decameters (Peru has high cities)
    return  Math.floor(elevationrandom * 360);
}   

function setup_controls(camera, baseElevation, mapscale){
    controls = new THREE.OrbitControls( camera );
    // farthest camera can zoom out
    controls.maxDistance = mapscale*1.5;
    // This sets the target that the camera focuses on
    controls.target.y=baseElevation; 
}

// buildCompass
// creates a simple red and blue compass showing sealevel, the center of the map, and north.
function buildCompass(scene){
    // Vertical Red Line
    var geometry = new THREE.BoxGeometry( 1, 10, 1 );
    var material = new THREE.MeshBasicMaterial( {color: 0x660000} );
    var line = new THREE.Mesh( geometry, material );
    line.position.y=-5;
    scene.add(line);

    // Horizontal Blue Line
    geometry = new THREE.BoxGeometry( 1, 1, 10 );
    material = new THREE.MeshBasicMaterial( {color: 0x000066} );
    line = new THREE.Mesh( geometry, material );
    line.position.z=5;
    scene.add(line);
}

// selectCityCenter
// selects a centerpoint for the city. This is where at least 2-3 of the largest roads meet.
function selectCityCenter(mapscale){
    var geometry = new THREE.BoxGeometry( 1, 3000, 1 );
    var material = new THREE.MeshBasicMaterial( {color: 0x006600} );
    var cube = new THREE.Mesh( geometry, material );
    // cast shadows to help visualize our lighting
    //cube.castShadow = true;
    //cube.receiveShadow = true;

    var range=0.1 ;// 10%
    // This will range from 40% to 60% if the range is 10%
    var lowrange=(0.5-range)*mapscale
    var highrange=(0.5+range)*mapscale

    var x = Math.random()*(highrange-lowrange) + lowrange - mapscale/2;
    var z = Math.random()*(highrange-lowrange) + lowrange - mapscale/2;
    cube.position.x=x;
    cube.position.z=z;
    console.log("City center located at ", x, ",", z, "which is somewhere between ", lowrange, " and ", highrange);
    return cube;
}

//place the camera
function addCamera(scene, mapscale, baseElevation){
    var zoom=0.3;
    camera.position.y = mapscale * zoom * 1.5 + baseElevation;
    camera.position.x = mapscale * zoom;
    camera.position.z = -mapscale * zoom;
}

// Add 3-point light theory implementation + ambient light. 
function addLights(scene, mapscale, baseElevation){
    var cameraradius=mapscale

    var light    = new THREE.AmbientLight(0x101010)
    light.name   = 'Ambient light'
    scene.add(light)

    var light    = new THREE.DirectionalLight('white', 0.7);
    light.name   = 'Key light'
    light.position.set(mapscale, mapscale+baseElevation, mapscale)
    light=configShadowbox(light, cameraradius, baseElevation);
    light.shadowDarkness = 0.6;
    light.shadowCameraVisible = false;
    scene.add(light)
    console.log( light)
    console.log( "baseEle", baseElevation)

    var light    = new THREE.DirectionalLight('white', 0.3)
    light.name   = 'Fill light'
    light.position.set(-mapscale, mapscale/4+baseElevation, mapscale)
    light=configShadowbox(light, cameraradius, baseElevation);
    light.shadowDarkness =0.25;
    light.shadowCameraVisible = false;
    scene.add(light)

    var light    = new THREE.DirectionalLight('white', 0.225)
    light.name   = 'Back light'
    light.position.set(0, mapscale/4+baseElevation, -mapscale)
    light = configShadowbox(light, cameraradius, baseElevation);
    light.shadowDarkness = 0.15;
    light.shadowCameraVisible = false;
    light.name   = 'Back light'
    scene.add(light)
}

// Each light has a shadowbox to determine when/where to cast shadows.
function configShadowbox(light, cameraradius, baseElevation){
    light.castShadow = true;
    light.target.y = baseElevation;
    light.shadowMapWidth=1024;
    light.shadowMapHeight=1024;
    light.shadowCameraFar = cameraradius*2.5;
    light.shadowCameraTop = cameraradius;
    light.shadowCameraBottom = -cameraradius;
    light.shadowCameraLeft = -cameraradius;
    light.shadowCameraRight = cameraradius;
    return light
}

// configure stats to show some basic info on the map displayed
function config_stats(seed, mapscale, baseElevation, elevationVariation){
    var stats = document.createElement( 'div' );
    stats.innerHTML = 'seed: '+seed+"<br>"+
                      "size: "+(mapscale/100)+"km<br>"+
                      "altitude: "+(baseElevation/100)+"km<br>"+
                      "variation: "+Math.round(elevationVariation*10)+"m";
    stats.style.position = 'absolute';
    stats.style.top = '0px';
    return stats;
}

// Transform a small canvas into a large canvas
function scaleTexture(smallcanvas, mapscale){

    // create fullsize canvas
    var largerCanvas = document.createElement( 'canvas' );
    largerCanvas.width = mapscale;
    largerCanvas.height = mapscale;

    // take what is in the small canvas and scale it to mapscale
    var context = largerCanvas.getContext( '2d' );
    context.scale( mapscale/smallcanvas.width, mapscale/smallcanvas.height );
    context.drawImage( smallcanvas, 0, 0 );

    return largerCanvas;
}

function mapTerrainToGeometry(geometry,terraindata){
    for ( var i = 0, l = geometry.vertices.length; i < l; i ++ ) {
        if (terraindata[ i ] > 0) {
            geometry.vertices[ i ].y = terraindata[ i ] ;
        }else{
            geometry.vertices[ i ].y = 0;
        }
    }
    return geometry;
}
