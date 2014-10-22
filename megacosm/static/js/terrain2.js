//
// A simple check to make sure we're not wasting everyone's time
//
if ( ! Detector.webgl ) {
    Detector.addGetWebGLMessage();
    document.getElementById( 'mapcontainer' ).innerHTML = "Sorry, you need WebGL enabled to see this.";
}

// boring resize function
function onWindowResize() {
    camera.aspect = mapcontainer.width / mapcontainer.height;
    camera.updateProjectionMatrix();
    renderer.setSize( mapcontainer.width, mapcontainer.height );
    controls.handleResize();
}

// boring animate
function animate() {
    requestAnimationFrame( animate );
    render();
}

// boring render
function render() {
    controls.update( clock.getDelta() );
    renderer.render( scene, camera );
}

function setup_controls(camera, baseElevation, mapscale){
    controls = new THREE.OrbitControls( camera );
    // farthest camera can zoom out
    controls.maxDistance = mapscale*1.5;
    // the speed in which it moves
    controls.movementSpeed = 100;
    // state flips pan and rotate buttons
    controls.state=2;
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
function selectCityCenter(mapscale, baseElevation){
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
function configShadowbox(light, cameraradius){
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
function config_stats(seed, mapscale, baseElevation){
    var stats = document.createElement( 'div' );
    stats.innerHTML = 'seed: '+seed+"<br>"+
                      "altitude: "+(baseElevation/100)+"km<br>"+
                      "diameter: "+(mapscale/100)+"km";
    stats.style.position = 'absolute';
    stats.style.top = '0px';
    return stats
}
