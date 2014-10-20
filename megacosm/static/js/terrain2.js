if ( ! Detector.webgl ) {
    Detector.addGetWebGLMessage();
    document.getElementById( 'mapcontainer' ).innerHTML = "Sorry, you need WebGL enabled to see this.";
}

function buildCompass(scene){
    var geometry = new THREE.BoxGeometry( 10, 1000, 10 );
    var material = new THREE.MeshBasicMaterial( {color: 0x660000} );
    var line = new THREE.Mesh( geometry, material );
    line.position.y=-500;
    line.castShadow = true;
    scene.add(line);

    geometry = new THREE.BoxGeometry( 10, 10, 1000 );
    material = new THREE.MeshBasicMaterial( {color: 0x000066} );
    line = new THREE.Mesh( geometry, material );
    line.position.z=500;
    line.castShadow = true;
    scene.add(line);
}

function selectCityCenter(mapscale){
    var geometry = new THREE.BoxGeometry( 10, 5000, 10 );
    var material = new THREE.MeshBasicMaterial( {color: 0x006600} );
    var cube = new THREE.Mesh( geometry, material );
    cube.castShadow = true;
    var scope=0.1 ;// 10%
    // This will range from 40% to 60% if the scope is 10%
    var x = Math.random()*(mapscale*(0.5+scope)-mapscale*(0.5-scope))+ mapscale*(0.5-scope) - mapscale/2;
    var z = Math.random()*(mapscale*(0.5+scope)-mapscale*(0.5-scope))+ mapscale*(0.5-scope) - mapscale/2;
    cube.position.x=x;
    cube.position.z=z;
    console.log("width range at " + mapscale*(0.5+scope) + "," + mapscale*(0.5-scope))
    console.log("center at " + x + "," + z);
    return cube;
}
function onWindowResize() {

    camera.aspect = mapcontainer.width / mapcontainer.height;
    camera.updateProjectionMatrix();
    renderer.setSize( mapcontainer.width, mapcontainer.height );

    controls.handleResize();

}

function animate() {
    requestAnimationFrame( animate );
    render();
}

function render() {
    controls.update( clock.getDelta() );
    renderer.render( scene, camera );
}

function setup_controls(camera){
    controls = new THREE.OrbitControls( camera );
    controls.maxDistance = 8000;
    controls.movementSpeed = 100;
    controls.state=2;
}
function addLights(scene){

    var object3d    = new THREE.AmbientLight(0x101010)
    object3d.name   = 'Ambient light'
    scene.add(object3d)

    var object3d    = new THREE.DirectionalLight('white', 0.7);
    object3d.name   = 'Key light'
    object3d.position.set(3500, 3500, 3500)
    object3d.castShadow = true;
    object3d.shadowDarkness =0.7;
    object3d.shadowMapWidth=1024;
    object3d.shadowMapHeight=1024;
    object3d.shadowCameraFar = 10000;
    object3d.shadowCameraTop = 5000;
    object3d.shadowCameraBottom = -5000;
    object3d.shadowCameraLeft = -5000;
    object3d.shadowCameraRight = 5000;
    object3d.shadowCameraVisible = false;
    scene.add(object3d)

    var object3d    = new THREE.DirectionalLight('white', 0.3)
    object3d.name   = 'Fill light'
    object3d.position.set(-3500,3500,3500)
    object3d.castShadow = true;
    object3d.shadowDarkness =0.35;
    object3d.shadowMapWidth=1024;
    object3d.shadowMapHeight=1024;
    object3d.shadowCameraFar = 10000;
    object3d.shadowCameraTop = 5000;
    object3d.shadowCameraBottom = -5000;
    object3d.shadowCameraLeft = -5000;
    object3d.shadowCameraRight = 5000;
    object3d.shadowCameraVisible = false;
    scene.add(object3d)
    var object3d    = new THREE.DirectionalLight('white', 0.225)
    object3d.name   = 'Back light'
    object3d.position.set(0,2000,-4300)
    object3d.castShadow = true;
    object3d.shadowDarkness =0.25;
    object3d.shadowMapWidth=1024;
    object3d.shadowMapHeight=1024;
    object3d.shadowCameraFar = 8000;
    object3d.shadowCameraTop = 5000;
    object3d.shadowCameraBottom = -5000;
    object3d.shadowCameraLeft = -5000;
    object3d.shadowCameraRight = 5000;
    object3d.shadowCameraVisible = false;
    object3d.name   = 'Back light'
    scene.add(object3d)

}
