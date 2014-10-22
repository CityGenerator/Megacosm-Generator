
// Seeds currently generate from 0-1000, which is an arbitrary limit;
// will be passed in from the backend later
var seed = Math.round(Math.random()*1000)
seed=605
// Seed random courtesy of seedrandom.min.js
Math.seedrandom(seed);

// Mapscales represent how big the square map is in kilometers
var mapscales=[ 1, 2, 5, 10, 25];

// mapscale units are decameters
//  1 =  100 decameters =  1 km
// 25 = 2500 decameters = 25 km
var mapscale= mapscales[Math.floor(Math.random()*mapscales.length)]*100;

// These 4 variables are unavoidable globals
var camera, controls, scene, renderer;

var terrain_lowpoint;
var terrain_highpoint;
var terrain_delta=0;

console.log("region size: ", (mapscale/100)*(mapscale/100), "square kilometers")

var clock = new THREE.Clock();
init();
animate();


function init() {

    /* Grab the map container and set the width */
    var mapcontainer = document.getElementById( 'mapcontainer' );
    // Set the base elevation for the map- is it seaside, or is it in the mountains?
    var baseElevation = generateBaseElevation();

    // Gives us 50-150 depending on mapscale.
    var variationMax = mapscale/24 + 45 + (5/6);

    // Gives us 0.1-0.5 depending on mapscale.
    var variationMin = mapscale/6000 + (1/12);

    // altitude varies according to the land area viewed;
    var elevationVariation = Math.random()*(variationMax-variationMin) + variationMin

    /* Set up the camera, scene and controls */
    camera = new THREE.PerspectiveCamera( 60, mapcontainer.offsetWidth / mapcontainer.offsetHeight, 1, 20000 );
    scene = new THREE.Scene();
    setup_controls(camera, baseElevation, mapscale);
    addLights(scene, mapscale, baseElevation);
    addCamera(scene, mapscale, baseElevation);

    /* Create a terrain mesh and add it to the scene*/
    var land = generateLand(mapscale, baseElevation, elevationVariation)
    //TODO generate roads on the map right here.
    scene.add(land);

    setup_renderer(mapcontainer);

    var stats = config_stats(seed, mapscale, baseElevation, elevationVariation)
    mapcontainer.appendChild( stats );

    window.addEventListener( 'resize', onWindowResize, false );
}

function generateElevationMap(mapscale, baseElevation, elevationVariation, resolution) {
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
    var scale = 50.0
    for ( var octave=1 ; octave <= octavecount ; octave++ ){
        var octavevalue=Math.pow(2,octave-1)*scale;
        for ( var i = 0; i < size; i ++ ) {
            var x = i % resolution, y = ~~ ( i / resolution );
            var noise = perlin.noise( x/octavevalue, y/octavevalue, z_slice ); // noise should range from -1 to 1
            if (isNaN(data[i])) {
                data[i] = 0
            }
            var amplitude=(octave/octavecount)
            data[i] = data[i] + noise*amplitude;
        }
    }
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
    var smallcanvas = document.createElement( 'canvas' );

    //note that terrain resolution is small
    smallcanvas.width = terrainResolution;
    smallcanvas.height = terrainResolution;

    // start with a black rectangle on a canvas
    var smallcontext = smallcanvas.getContext('2d');
    smallcontext.fillRect(0, 0, terrainResolution, terrainResolution);
    smallcontext.fillStyle = '#000';
    // Create an image to color
    var smallimage = smallcontext.getImageData( 0, 0, terrainResolution, terrainResolution);
    // apply our color palette to the image that will be mapped
    smallimage = colorTerrainImage(smallimage, terraindata)
    // apply our new colors to the context image
    smallcontext.putImageData( smallimage, 0, 0 );
 
    return scaleTexture(smallcanvas, mapscale);

}
function colorTerrainImage(image, terraindata){
    //imageData is a 65536 element array-like object full of stuff (I guess)
    var imageData = image.data;

    // loop through the length of the image by 4colors a go.
    // i = pixel color position in image (rgba, hence counting by 4)
    // j = counter for terraindata
    for ( var i = 0, j = 0 ; i < imageData.length ; i += 4, j ++ ) {
        var datadelta = terraindata[j] - terrain_lowpoint;
        var percentage_delta = datadelta / terrain_delta;

        // Set the base color to red, just in case
        // If imageData was a real array, we could splice these in. alas, it's undefined.
        imageData[ i ] = 255;
        imageData[ i + 1 ] = 0;
        imageData[ i + 2 ] = 0;

        // atp and tcolor are defined in env_setup.js, where they are very nicely formatted.
        // atp = altitude Transition Points
        // atp is an array of numbers arranged from highest to lowest
        // tcolor = transition color
        // tcolor is an array of rgb triplets representing altitude transition colors (white, brown, green, blue))
        // Note that each tcolor correlates to an atp value

        //Loop through each atp, note the intentional use of 1 rather than 0 to prevent an overrun when comparing atp points
        for (var transitionID=1; transitionID< atp.length; transitionID++){
            // if the current elevation is between these two transition points
            if (terraindata[j] > atp[transitionID] && terraindata[j] <= atp[transitionID-1] ){

                //  find distance between transition points
                var distance = atp[transitionID-1] - atp[transitionID];

                // find distance between terrain altitude and lowest transition point
                var place = terraindata[j] - atp[transitionID];

                // calculate how far the terrain point is from the lower transition point
                var percentage = place/distance;

                // calculate the proper color based on distance between two transition points
                var color=gradient_color(tcolors[transitionID-1],tcolors[transitionID],percentage);

                // apply RGB values to imageData
                imageData[ i ]     = color[0];
                imageData[ i + 1 ] = color[1];
                imageData[ i + 2 ] = color[2];
                // Once we've found this pixel's transition location, we can break out of the loop.
                break;
            }
        }
    }
    return image
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


function generateLand(mapscale, baseElevation,elevationVariation ) {

    // how smooth it looks. increasing this adds compute time exponentially
    var terrainResolution=512;

    /*note that the x and y need to be stretched from the resolution to the mapscale */
    var terraindata  = generateElevationMap(mapscale, baseElevation, elevationVariation, terrainResolution);

    // our terrain geometry is mapscale x mapscale, with terrainResolution-1 segments in each direction.
    var geometry = new THREE.PlaneGeometry( mapscale, mapscale, terrainResolution - 1, terrainResolution - 1  );

    // initial geometry creation is vertical;
    // We are rotating the geometry so that Y is height, z is depth and X is width.
    geometry.applyMatrix( new THREE.Matrix4().makeRotationX( - Math.PI / 2 ) );

    //map the altitude changes to the geometry
    geometry = mapTerrainToGeometry(geometry, terraindata);

    var textureMap = generateTexture(terraindata,terrainResolution, mapscale);

    var texture = new THREE.Texture(textureMap, new THREE.UVMapping(), THREE.ClampToEdgeWrapping, THREE.ClampToEdgeWrapping );
    texture.needsUpdate = true;

    var terrainmesh = new THREE.Mesh( geometry, new THREE.MeshLambertMaterial( { map: texture } ) );
    terrainmesh.castShadow = true;
    terrainmesh.receiveShadow = true;

    return terrainmesh
}

