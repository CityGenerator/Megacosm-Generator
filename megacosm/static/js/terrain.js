
var seed = Math.round(Math.random()*100)
//seed=51
Math.seedrandom(seed);
var mapscales=[0.05, 0.1, 0.2, 0.5, 1.0, 2.5];

// What if 1 unit was a decameter rather than a meter?

var mapscale= 1000// mapscales[Math.floor(Math.random()*mapscales.length)]*1000;
var terrainResolution=256;

var mapcontainer, camera, controls, scene, renderer,stats;
var terrain_lowpoint;
var terrain_highpoint;
var terrain_delta=0;

console.log("region size: ", mapscale,",", mapscale,"; ", (mapscale/1000)*(mapscale/1000), "square kilometers")

var clock = new THREE.Clock();
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
    /*note that the x and wy need to be stretched from the resolution to the mapscale */
    var terrainMap  = generateElevationMap(terrainResolution, mapscale);
    var terrainMesh = generateTerrainMesh(mapscale, terrainResolution, terrainMap)
    scene.add(terrainMesh);

    var citymarker=selectCityCenter(mapscale);
    scene.add(citymarker);

    buildCompass(scene);

    addLights(scene);

    camera.position.y = 3000 ;
    camera.position.x = 2000 ;
    camera.position.z = -2000 ;

    renderer = new THREE.WebGLRenderer({antialias: true});
    renderer.setClearColor( 0xbfd1e5 );
    renderer.setSize( mapcontainer.width, mapcontainer.height );
    renderer.shadowMapEnabled = true;
    renderer.shadowMapType = THREE.PCFSoftShadowMap;


    stats = document.createElement( 'div' );
    stats.innerHTML = 'seed '+seed;
    stats.style.position = 'absolute';
    stats.style.top = '0px';
    mapcontainer.appendChild( stats );

    mapcontainer.appendChild( renderer.domElement );

    window.addEventListener( 'resize', onWindowResize, false );
}



function generateElevationMap(resolution, mapscale) {
    // resolution is 256x256
    // size is 65536
    var size = resolution*resolution;
    var data = [];
    perlin = new ImprovedNoise()
    // TODO base elevation and variation both need to be skewed. look into gamma curve correction
    var z_slice = Math.random() * 100;  // Determines region of noise to slice from
    var octavecount=4;

    // forget the actual terrain, just map the noise
    // TODO amplitude should be proportional to octave
    for ( var octave=0 ; octave < octavecount ; octave++ ){
        var octavevalue=Math.pow(2,octave)*1.0;
        for ( var i = 0; i < size; i ++ ) {
            var x = i % resolution, y = ~~ ( i / resolution );
            var noise = perlin.noise( x/200*octavevalue, y/200*octavevalue, z_slice ); // noise should range from -1 to 1
            if (isNaN(data[i])) {
                data[i] = noise;
            }else{
                data[i] = data[i] + noise;
            }
        }
        console.log("last elevation for octave ",octave,":",data[size-1])
    }

    // REMEMBER, these are in decameters

//    var elevationrandom = Math.pow(Math.random(), 2);
    var elevationrandom = -Math.log(Math.random())
    var elevationrandom =1.1*Math.sin(1.5*(Math.random())-1.6)+1.1;
    console.log('#################### ', elevationrandom)
    var baseElevation =  Math.floor(elevationrandom * 360);    // Starting elevation, between 0 and 5000 meters (Peru has high cities)

    // Altitude ranges from 0-6 for a 1000km square to 0-150 for a 25000km square
    var elevationVariation = Math.floor(Math.random() * 150*(mapscale/2500)); // variation in altitude from 0 to 1500 meters (LA has mountains apparently)
    // XXX 3500 above should be 1500; testing varying elevation.
    terrain_highpoint=baseElevation - elevationVariation;
    terrain_lowpoint=baseElevation + elevationVariation;
    console.log("base elevation and variation :", baseElevation, elevationVariation)
    console.log("initial low and high (these will flip) :", terrain_lowpoint, terrain_highpoint)

    // Now that the noise is settled, loop through once more to convert it to an elevation;
    for ( var i = 0; i < size; i ++ ) {
        var variance=Math.round(  data[i]*elevationVariation  ,2  );
        data[i] = baseElevation + variance;
//        console.log("base + variance = elevation ", baseElevation, variance, data[i] )

        if (data[i] < terrain_lowpoint){terrain_lowpoint=data[i]};
        if (data[i] > terrain_highpoint){terrain_highpoint=data[i] };
    }
    console.log("last elevation:",data[size-1])
    terrain_delta=terrain_highpoint-terrain_lowpoint;
    console.log("final terrain low/high and delta: ",terrain_lowpoint,terrain_highpoint, terrain_delta)
    return data;
}

function generateTexture( terraindata, terrainResolution, mapscale ) {

    // Canvas is a representation of the skin we're about to create
    // not an actaul canvas element that will be used
    var canvas = document.createElement( 'canvas' );
    //note that terrain resolution is only 256
    canvas.width = terrainResolution;
    canvas.height = terrainResolution;

    // start with a 256x256 black rectangle on a canvas
    var context = canvas.getContext('2d');
    context.fillStyle = '#000';
    context.fillRect(0, 0, terrainResolution, terrainResolution);

    // Create a 256x256 image
    var image = context.getImageData( 0, 0, terrainResolution,terrainResolution );
    //imageData is a 65536 element array full of stuff (I guess)
    var imageData = image.data;

    // loop through the length of the image by 4colors a go.
    // i = pixel color position in image (rgba, hence counting by 4)
    // j = counter for terraindata
    for ( var i = 0, j = 0 ; i < imageData.length ; i += 4, j ++ ) {
        var datadelta = terraindata[j] - terrain_lowpoint;
        var percentage_delta = datadelta / terrain_delta;
        
        // REMEMBER, we've switched to Decameters
        if (terraindata[j] < terrain_lowpoint){
            // This is just to make sure terrain data doesn't go lower than the low point- it'll be bright red
            imageData[ i ] = 255;
            imageData[ i + 1 ] = 0;
            imageData[ i + 2 ] = 0;
        } else if (terraindata[j] >500){
            // mountain tops are white TODO add a 5% chance of brown for realism
            imageData[ i ] = 255;
            imageData[ i + 1 ] = 255;
            imageData[ i + 2 ] = 255;
        } else if (terraindata[j] <=500 && terraindata[j] >300 ){
            // white to red rock
            var percentage= (terraindata[j]-300)/200
            var transientcolor=gradient_color([255,255,255],[152,2,2],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        } else if (terraindata[j] <=300 && terraindata[j] >200 ){
            // red rock to brown
            var percentage= (terraindata[j]-200)/100
            var transientcolor=gradient_color([152,2,2],[161,68,1],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        } else if (terraindata[j] <=200 && terraindata[j] >50 ){
            var percentage= (terraindata[j]-50)/150
            var transientcolor=gradient_color([161,68,1],[203, 185, 107],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        } else if (terraindata[j] <=50 && terraindata[j] >1 ){
            var percentage= (terraindata[j]-1)/49
            var transientcolor=gradient_color([203, 185, 107],[15, 120, 48],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        } else if (terraindata[j] <=1 && terraindata[j] >0 ){
            var percentage= (terraindata[j])/1
            var transientcolor=gradient_color([15, 120, 48],[0, 99, 70],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        //WATER!
        } else if (terraindata[j] <=0 && terraindata[j] >-0.5 ){
            var percentage= (0.5+terraindata[j])/0.5
            var transientcolor=gradient_color([254, 171, 127],[203, 185, 107],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        } else if (terraindata[j] <=-0.5 && terraindata[j] >-2 ){
            var percentage= (2+terraindata[j])/1.5
            var transientcolor=gradient_color([203, 185, 107],[76, 193, 203],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        } else if (terraindata[j] <=-2 && terraindata[j] >-15 ){
            var percentage= (15+terraindata[j])/13
            var transientcolor=gradient_color([76, 193, 203],[54, 154, 212],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        } else if (terraindata[j] <=-15 && terraindata[j] >-100 ){
            var percentage= (100+terraindata[j])/85
            var transientcolor=gradient_color([54, 154, 212],[15, 120, 48],percentage);
            imageData[ i ] = transientcolor[0];
            imageData[ i + 1 ] = transientcolor[1];
            imageData[ i + 2 ] = transientcolor[2];
        }
        else{
            imageData[ i ] = 255;
            imageData[ i + 1 ] = 255;
            imageData[ i + 2 ] = 0;
        }
 
    }
    console.log("image contains:", imageData.length," color bits")
    context.putImageData( image, 0, 0 );
    
    // create fullsize canvas
    var canvasScaled = document.createElement( 'canvas' );
    canvasScaled.width = mapscale;
    canvasScaled.height = mapscale;
    context = canvasScaled.getContext( '2d' );

    // whatever image is written, scale it by 3.9
    context.scale( mapscale/terrainResolution, mapscale/terrainResolution );
    context.drawImage( canvas, 0, 0 );

    image = context.getImageData( 0, 0, terrainResolution, terrainResolution );
    imageData = image.data;

    // I have no idea what this does; commenting it out out of fear.
    for ( var i = 0, l = imageData.length; i < l; i += 4 ) {
        var v = ~~ ( Math.random() * 5 );
        imageData[ i ] += v;
        imageData[ i + 1 ] += v;
        imageData[ i + 2 ] += v;
    }

    context.putImageData( image, 0, 0 );
    return canvasScaled;
}


function gradient_color(colora, colorb, percentage ){
    
    var newcolor = [];
    for (var i = 0; i<3; i++){
        // For each color, determine the variance
        var variance=(colora[i]-colorb[i]);
        // multiply the variance * the percentage, round, then add back to first color
        newcolor[i] = colorb[i] + Math.round(variance*percentage)

    }
    return newcolor
}


function generateTerrainMesh(mapscale, terrainResolution, terraindata ) {

    var geometry = new THREE.PlaneGeometry( mapscale, mapscale, terrainResolution - 1, terrainResolution - 1  );
    geometry.applyMatrix( new THREE.Matrix4().makeRotationX( - Math.PI / 2 ) );

    for ( var i = 0, l = geometry.vertices.length; i < l; i ++ ) {
        if (terraindata[ i ] > 0) {
            geometry.vertices[ i ].y = terraindata[ i ] ;
        }else{
            geometry.vertices[ i ].y = 0;
        }
    }

    var texture = new THREE.Texture( generateTexture( terraindata, terrainResolution, mapscale ), new THREE.UVMapping(), THREE.ClampToEdgeWrapping, THREE.ClampToEdgeWrapping );
    texture.needsUpdate = true;

    var terrainmesh = new THREE.Mesh( geometry, new THREE.MeshLambertMaterial( { map: texture } ) );
    terrainmesh.castShadow = true;
    terrainmesh.receiveShadow = true;

    return terrainmesh
}


