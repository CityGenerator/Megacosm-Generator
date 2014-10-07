
if ( ! Detector.webgl ) {
    Detector.addGetWebGLMessage();
    document.getElementById( 'mapcontainer' ).innerHTML = "Sorry, you need WebGL enabled to see this.";
}
var mapcontainer;
var camera, controls, scene, renderer;

var worldWidth = 256, worldLength = 256,
worldHalfWidth = worldWidth / 2, worldHalfLength = worldLength / 2;

var clock = new THREE.Clock();
Math.seedrandom();
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
    var terrain = generate_terrain_mesh(worldWidth, worldLength);
    scene.add( terrain );

//                var plane = new THREE.Mesh(new THREE.PlaneGeometry(2500, 2500), new THREE.MeshNormalMaterial());
//                plane.overdraw = true;
//                plane.rotation.y=90;
//                scene.add(plane);
 

    camera.position.y = data[ worldHalfWidth + worldHalfLength * worldWidth ] * 10 + 20500;

    renderer = new THREE.WebGLRenderer();
    renderer.setClearColor( 0xbfd1e5 );
    renderer.setSize( mapcontainer.width, mapcontainer.height );

    mapcontainer.appendChild( renderer.domElement );

    window.addEventListener( 'resize', onWindowResize, false );
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

    var randval = Math.random();
    var scope_selection = randval * altitudescope.length;

    var scope = altitudescope[ Math.floor(scope_selection) ];

    console.log( altitudescope.length + " * "+randval +" ="+ scope_selection+ " resulting in "+ scope);

    var size = width * height, data = new Uint8Array( size ),
    perlin = new ImprovedNoise(), quality = scope, z = Math.random() * 100;

    for ( var j = 4; j > 0; j -- ) {

        for ( var i = 0; i < size; i ++ ) {

            var x = i % width, y = ~~ ( i / width );
            var noise=Math.abs( perlin.noise( x / quality, y / quality, z ));

            data[ i ] += Math.abs( noise  * quality);
        }
        quality *= 5;

    }

    for ( var i = 0; i < size; i ++ ) {
        data[ i ] =data[i]* scope;
    }
    return data;

}

function generateTexture( data, width, height ) {

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

    for ( var i = 0, j = 0, l = imageData.length; i < l; i += 4, j ++ ) {

        vector3.x = data[ j - 2 ] - data[ j + 2 ];
        vector3.y = 2;
        vector3.z = data[ j - width * 2 ] - data[ j + width * 2 ];
        vector3.normalize();

        shade = vector3.dot( sun );

        imageData[ i ] = ( 96 + shade * 128 ) * ( 0.5 + data[ j ] * 0.007 );
        imageData[ i + 1 ] = ( 32 + shade * 96 ) * ( 0.5 + data[ j ] * 0.007 );
        imageData[ i + 2 ] = ( shade * 96 ) * ( 0.5 + data[ j ] * 0.007 );
    }

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

//

function animate() {
    requestAnimationFrame( animate );
    render();
}

function render() {
    controls.update( clock.getDelta() );
    renderer.render( scene, camera );
}


function generate_terrain_mesh(worldWidth, worldLength) {
    data = generateHeight( worldWidth, worldLength );
    var geometry = new THREE.PlaneGeometry( 7500, 7500, worldWidth - 1, worldLength - 1 );
    geometry.applyMatrix( new THREE.Matrix4().makeRotationX( - Math.PI / 2 ) );

    for ( var i = 0, l = geometry.vertices.length; i < l; i ++ ) {
        geometry.vertices[ i ].y = data[ i ] * 10;
    }

    var texture = new THREE.Texture( generateTexture( data, worldWidth, worldLength ), new THREE.UVMapping(), THREE.ClampToEdgeWrapping, THREE.ClampToEdgeWrapping );
    texture.needsUpdate = true;

    return new THREE.Mesh( geometry, new THREE.MeshBasicMaterial( { map: texture } ) );
}

function setup_controls(camera){
    controls = new THREE.OrbitControls( camera );
    controls.maxDistance = 8000;
    controls.movementSpeed = 100;
    controls.state=2;
}

