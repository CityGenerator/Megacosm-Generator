if ( ! Detector.webgl ) {
    Detector.addGetWebGLMessage();
    document.getElementById( 'mapcontainer' ).innerHTML = "Sorry, you need WebGL enabled to see this.";
}



var mapscales=[0.5, 1, 2, 5, 10, 25];

var mapscale=mapscales[1];

var mapcontainer;
var camera, controls, scene, renderer;
var terrain_lowpoint=0;
var terrain_highpoint=0;
var regionwidth=mapscale*1000;
var regionheight=mapscale*1000;

console.log("region size:", regionheight,",", regionwidth,"; ", mapscale*2, "")
// each width unit * 10 is a geometry unit
var worldWidth = 256, worldLength = 256,
worldHalfWidth = worldWidth / 2, worldHalfLength = worldLength / 2;

var clock = new THREE.Clock();
Math.seedrandom(98);
init();
animate();



function init() {

    /* Grab the map container and set the width */
    mapcontainer = document.getElementById( 'mapcontainer' );
    mapcontainer.width=600;
    mapcontainer.height=400;
    
    /* Set up the camera, scene and controls */
    camera = new THREE.PerspectiveCamera( 60, mapcontainer.width / mapcontainer.height, 1, 20000 );
    scene = new THREE.Scene();
    setup_controls(camera);

    /* Create a terrain mesh and add it to the scene*/
    var terrainmap  = generateHeight( worldWidth, worldLength );

    scene.add(generate_terrain_mesh(worldWidth, worldLength, terrainmap));

    scene.add(select_city_center(worldWidth, worldLength));

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

    camera.position.y = terrainmap[ worldHalfWidth + worldHalfLength * worldWidth ]*10 + 20500;


    renderer = new THREE.WebGLRenderer({antialias: true});
    renderer.setClearColor( 0xbfd1e5 );
    renderer.setSize( mapcontainer.width, mapcontainer.height );
    renderer.shadowMapEnabled = true;
    renderer.shadowMapType = THREE.PCFSoftShadowMap;

    mapcontainer.appendChild( renderer.domElement );

    window.addEventListener( 'resize', onWindowResize, false );
}

function select_city_center(worldWidth, worldLength){
    var geometry = new THREE.BoxGeometry( 30, 1000, 30 );
    var material = new THREE.MeshBasicMaterial( {color: 0x006600} );
    var cube = new THREE.Mesh( geometry, material );
    cube.castShadow = true;
    var scope=0.1 ;// 10%
    // This will range from 40% to 60% if the scope is 10%
    var x = Math.random()*(regionwidth*(0.5+scope)-regionwidth*(0.5-scope))+ regionwidth*(0.5-scope) - regionwidth/2;
    var z = Math.random()*(regionheight*(0.5+scope)-regionheight*(0.5-scope))+ regionheight*(0.5-scope) - regionheight/2;
    cube.position.x=x;
    cube.position.z=z;
    console.log("width range at " + regionwidth*(0.5+scope) + "," + regionwidth*(0.5-scope))
    console.log("center at " + x + "," + z);
    return cube;
}

function onWindowResize() {

    camera.aspect = mapcontainer.width / mapcontainer.height;
    camera.updateProjectionMatrix();
    renderer.setSize( mapcontainer.width, mapcontainer.height );

    controls.handleResize();

}

function generateHeight( width, height ) {
    /* Given a map of width x height, generate a single array
       that represents the height*/
    var altitudescope = [ 0.20, 0.25, 0.27, 0.3, 0.5, 1 ];

    altitudescope=[1]
    var randval = Math.random();
    var scope_selection = randval * altitudescope.length;

    var scope = altitudescope[ Math.floor(scope_selection) ];

    console.log( altitudescope.length + " * "+randval +" ="+ scope_selection+ " resulting in "+ scope);

    var size = width * height, data = new Uint8Array( size ),
    perlin = new ImprovedNoise(), quality = scope, z = Math.random() * 100;
    var octaves = 5

    for ( var j = octaves; j > 0; j -- ) {

        for ( var i = 0; i < size; i ++ ) {

            var x = i % width, y = ~~ ( i / width );
            var noise=Math.abs( perlin.noise( x / quality, y / quality, z ));

            data[ i ] += Math.abs( noise  * quality);
        }
        quality *= 5;

    }

    for ( var i = 0; i < size; i ++ ) {
        data[i] = data[i] * scope;
        if (data[i] < terrain_lowpoint){terrain_lowpoint=data[i]};
        if (data[i] > terrain_highpoint){terrain_highpoint=data[i] };
    }
    console.log(terrain_lowpoint,terrain_highpoint)
    return data;
}

function generateTexture( terraindata, width, height ) {

    var canvas, canvasScaled, context, image, imageData,
    level, diff, vector3, sun, shade;

    vector3 = new THREE.Vector3( 0, 0, 0 );

    sun = new THREE.Vector3( 1, 1, 1 );
    sun.normalize();

    canvas = document.createElement( 'canvas' );
    canvas.width = width;
    canvas.height = height;

    context = canvas.getContext( '2d' );
    context.fillStyle = '#000';
    context.fillRect( 0, 0, width, height );

    image = context.getImageData( 0, 0, canvas.width, canvas.height );
    imageData = image.data;

    var frostline=Math.random()+0.5;
    for ( var i = 0, j = 0, l = imageData.length; i < l; i += 4, j ++ ) {

        vector3.x = terraindata[ j - 2 ] - terraindata[ j + 2 ];
        vector3.y = 2;
        vector3.z = terraindata[ j - width * 2 ] - terraindata[ j + width * 2 ];
        vector3.normalize();

        shade = vector3.dot( sun );

        // image data determines color...
        //var terrain_lowpoint=0;
        //var terrain_highpoint=0;
        var delta=terrain_highpoint-terrain_lowpoint
        var datadelta= terraindata[j] - terrain_lowpoint
        var percentage= datadelta/delta;

        // data
        // If the frostline is 70%...
        imageData[ i ] = ( 96 + shade * 128 ) * ( 0.5 + terraindata[ j ] * 0.007 );
        imageData[ i + 1 ] = ( 32 + shade * 96 ) * ( 0.5 + terraindata[ j ] * 0.007 );
        imageData[ i + 2 ] = ( shade * 96 ) * ( 0.5 + terraindata[ j ] * 0.007 );
        if (percentage < frostline ){
            imageData[ i ] = 0 + terraindata[ j ];
            imageData[ i + 1 ] = 80;
            imageData[ i + 2 ] = 0 + terraindata[ j ];

        }else if (percentage > frostline){
            imageData[ i ] = 255;
            imageData[ i + 1 ] = 255;
            imageData[ i + 2 ] = 255;
        }
 
    }
//XXX
    context.putImageData( image, 0, 0 );

    // Scaled 4x

    canvasScaled = document.createElement( 'canvas' );
    canvasScaled.width = width * 4;
    canvasScaled.height = height * 4;

    context = canvasScaled.getContext( '2d' );
    context.scale( 4, 4 );
    context.drawImage( canvas, 0, 0 );

    image = context.getImageData( 0, 0, canvasScaled.width, canvasScaled.height );
    imageData = image.data;

    for ( var i = 0, l = imageData.length; i < l; i += 4 ) {

        var v = ~~ ( Math.random() * 5 );
        imageData[ i ] += v;
        imageData[ i + 1 ] += v;
        imageData[ i + 2 ] += v;
    }

    context.putImageData( image, 0, 0 );
    return canvasScaled;
}

function animate() {
    requestAnimationFrame( animate );
    render();
}

function render() {
    controls.update( clock.getDelta() );
    renderer.render( scene, camera );
}

function generate_terrain_mesh(worldWidth, worldLength, terraindata ) {
    var geometry = new THREE.PlaneGeometry( regionwidth, regionheight, worldWidth - 1, worldLength - 1 );
    geometry.applyMatrix( new THREE.Matrix4().makeRotationX( - Math.PI / 2 ) );

    for ( var i = 0, l = geometry.vertices.length; i < l; i ++ ) {
        geometry.vertices[ i ].y = terraindata[ i ] * 10;
    }

    var texture = new THREE.Texture( generateTexture( terraindata, worldWidth, worldLength ), new THREE.UVMapping(), THREE.ClampToEdgeWrapping, THREE.ClampToEdgeWrapping );
    texture.needsUpdate = true;

    var terrainmesh = new THREE.Mesh( geometry, new THREE.MeshLambertMaterial( { map: texture } ) );
    terrainmesh.castShadow = true;
    terrainmesh.receiveShadow = true;

    return terrainmesh
}

function setup_controls(camera){
    controls = new THREE.OrbitControls( camera );
    controls.maxDistance = 8000;
    controls.movementSpeed = 100;
    controls.state=2;
}


