
// Seeds currently generate from 0-1000, which is an arbitrary limit;
// will be passed in from the backend later
var seed = Math.round(Math.random()*1000)

// Seed random courtesy of seedrandom.min.js
Math.seedrandom(seed);

// Mapscales represent how big the square map is in kilometers
var mapscales=[ 1, 2, 5, 10, 25];

// Units are decameters
var mapscale= mapscales[Math.floor(Math.random()*mapscales.length)]*100;

//2.5 = 2500 decameters = 25 km
//0.1= 100 decameters = 1 km

// FIXME this is a sloppy way to skew elevation to be low...
var elevationrandom =1.1*Math.sin(1.5*(Math.random())-1.6)+1.1;

// Starting elevation, between 0 and 360 decameters (Peru has high cities)
var baseElevation =  Math.floor(elevationrandom * 360);

// how smooth it looks. increasing this adds compute time exponentially
var terrainResolution=512;

var mapcontainer, camera, controls, scene, renderer,stats;
var terrain_lowpoint;
var terrain_highpoint;
var terrain_delta=0;

console.log("region size: ", (mapscale/100)*(mapscale/100), "square kilometers")

var clock = new THREE.Clock();
init();
animate();


function init() {

    /* Grab the map container and set the width */
    mapcontainer = document.getElementById( 'mapcontainer' );
    mapcontainer.width=800;
    mapcontainer.height=600;
    
    /* Set up the camera, scene and controls */
    camera = new THREE.PerspectiveCamera( 60, mapcontainer.width / mapcontainer.height, 1, 20000 );
    scene = new THREE.Scene();
    setup_controls(camera, baseElevation, mapscale);

    /* Create a terrain mesh and add it to the scene*/
    /*note that the x and wy need to be stretched from the resolution to the mapscale */
    var elevationMap  = generateElevationMap(terrainResolution, mapscale, baseElevation);
    var terrainMesh = generateTerrainMesh(mapscale, terrainResolution, elevationMap)
    scene.add(terrainMesh);

    var citymarker=selectCityCenter(mapscale, baseElevation);
    scene.add(citymarker);

    //buildCompass(scene);

    addLights(scene, mapscale, baseElevation);
    addCamera(scene, mapscale, baseElevation);

    renderer = new THREE.WebGLRenderer({antialias: true});
    renderer.setClearColor( 0xbfd1e5 );
    renderer.setSize( mapcontainer.width, mapcontainer.height );
    renderer.shadowMapEnabled = true;
    renderer.shadowMapType = THREE.PCFSoftShadowMap;
    mapcontainer.appendChild( renderer.domElement );

    stats = config_stats(seed, mapscale, baseElevation)
    mapcontainer.appendChild( stats );

    window.addEventListener( 'resize', onWindowResize, false );
}

function generateElevationMap(resolution, mapscale, baseElevation) {
    // resolution is 256x256
    // size is 65536
    var size = resolution*resolution;
    var data = [];
    perlin = new ImprovedNoise()
    var z_slice = Math.random() * 100;  // Determines region of 3d noise to slice from
    var octavecount=5;

    // forget the actual elevation, just map the noise
    // Octave 1 should be zoomed out the most, lots of variation, little amplitude
    // octave 2 should be zoomed in, less variation more amplitude
    // octave 3 should be more zoomed, even less variation, even more amplitude
    var scale=50.0
    for ( var octave=1 ; octave <= octavecount ; octave++ ){
        var octavevalue=Math.pow(2,octave-1)*scale;
        for ( var i = 0; i < size; i ++ ) {
            var x = i % resolution, y = ~~ ( i / resolution );
            var noise = perlin.noise( x/octavevalue, y/octavevalue, z_slice ); // noise should range from -1 to 1
            if (isNaN(data[i])) {
                data[i]=0
            }
            var amplitude=(octave/octavecount)
            data[i] = data[i] + noise*amplitude;
        }
    }

    // REMEMBER, these are in decameters
    // altitude varies according to the land area viewed;
    // NOTE: mapscale between 100 decameters and 2500 decameters
    var variationMax=mapscale/24 + 45 +(5/6)  // Gives us 50-150 depending on size.
    var variationMin=mapscale/6000 +(1/12)  // Gives us 0.1-0.5 depending on size.
    var elevationVariation= Math.random()*(variationMax-variationMin) + variationMin
    console.log("varmin, varmax, vartotal: ",variationMin,variationMax,elevationVariation)

    terrain_highpoint=baseElevation - elevationVariation;
    terrain_lowpoint=baseElevation + elevationVariation;

    // Now that the noise is settled, loop through once more to convert it to an elevation;
    for ( var i = 0; i < size; i ++ ) {
        var variance=  data[i]*elevationVariation  ;
        data[i] = baseElevation + variance;

        if (data[i] < terrain_lowpoint){terrain_lowpoint=data[i]};
        if (data[i] > terrain_highpoint){terrain_highpoint=data[i] };
    }
    terrain_delta=terrain_highpoint-terrain_lowpoint;
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

        // Set the base color to red, just in case
        imageData[ i ] = 255;
        imageData[ i + 1 ] = 0;
        imageData[ i + 2 ] = 0;
        
        // REMEMBER, we've switched to Decameters
        // altitude Transition Points
        
        var atp=[
                1000, //snowiest, 360+150 should be way under 1000, but it's here just in case
                550, //snow
                400, //light rocks
                300, // rocky
                250, //pine
                100, //olive
                60,  //decid
                10,  //marsh
                1,   //blah grass
                0.5, //yellow sand
                0,   //pink sand
                -.5, //ocean spray water
                -1,  //shallow water
                -15, // midwater
                -100, //deepwater
                -1000, //deepwater
                ]
        var tcolors=[ 
                        [255,255,255], //snow
                        [255,255,226], //snow
                        [241, 213, 192],   //lighrock
                        [118, 87, 33],   // rock
                        [115, 145, 93],   //pine
                        [71, 99, 2],   //  olive tree
                        [39, 120, 15],   //decid
                        [0, 102, 51],   //marsh
                        [75, 107, 70],   // blah grass
                        
                        [229, 207, 185],   //pink sand
                        [112, 102, 79],   // brown sand

                        [136, 181, 190],   //ocean spray water
                        [30, 67, 81],   // shallow water
                        [0, 42, 81], //midwater
                        [0, 0, 81],   // deep water
                        [0, 0, 81],   // deep water
                    ]
            //Loop through each atp, note the intentional use of 1 rather than 0 to create the offset
            for (var tran=1; tran< atp.length; tran++){
                // if the current elevation is between these two transition points
                if (terraindata[j] > atp[tran] && terraindata[j] <= atp[tran-1] ){
                    var difference = atp[tran-1] - atp[tran]; // should always be a positive number
                    var place = terraindata[j] - atp[tran]; //  atp[tran] should always be smaller, so place is positive
                    var percentage = place/difference;      //represents the location between atp[tran-1] and atp[tran]

                    var color=gradient_color(tcolors[tran-1],tcolors[tran],percentage);
                    imageData[ i ]     = color[0];
                    imageData[ i + 1 ] = color[1];
                    imageData[ i + 2 ] = color[2];
                    break;
                }
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

    context.putImageData( image, 0, 0 );
    return canvasScaled;
}


function gradient_color(colora, colorb, percentage ){
    
    // fudge causes altitude-unrelated variation within a gradient.
    if (Math.random() > .95){
        // 1 in 20 change of something odd appearing
        percentage=Math.max(0,Math.min(1, percentage + (Math.random() - 0.5)) )
    }
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


