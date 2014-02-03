
// Yes, I'm using a lot of document.blah globals. feel free to improve it.

function generate_scene() {


    // Lets set aside some useful variables...

    var planetwindow = document.getElementById('planetwindow');
    var WIDTH  = parseInt(planetwindow.style.width),
        HEIGHT = parseInt(planetwindow.style.height);



    // We need a scene
    document.scene = new THREE.Scene();
    // A Camera
    document.camera = new THREE.PerspectiveCamera(45, WIDTH / HEIGHT, 0.1, 100);
    document.camera.position.z = 1.5;
    // And a renderer
    document.renderer = new THREE.WebGLRenderer();
    document.renderer.setSize(WIDTH, HEIGHT);

    //Then lets throw a background up for flavor
    background = createBackground(90, 64);
    document.scene.add(background);


    // Add the control features
    document.controls = new THREE.TrackballControls(document.camera);

    // add our new renderer to our div
    planetwindow.appendChild(document.renderer.domElement);
}



function generate_stars(worldId){
    //A little ambient light to see stuff on the back side.
    document.scene.add(new THREE.AmbientLight(0x444444));

    // Lets replicate the light of a single star to start with.
    var light = new THREE.DirectionalLight(0xffffff, 0.7);
    light.position.set(10,2,10);
    document.scene.add(light);

}



function generate_planet(worldId){
    // planet params
    var radius   = 0.5,
        segments = 30;


    // We need to create two parts,
    document.planet = createPlanet(radius, segments, worldId);
    document.planet.rotation.y = 0;
    document.scene.add(document.planet)

    document.clouds = createClouds(radius+0.01, segments);
    document.clouds.rotation.y = 0;
    document.scene.add(document.clouds)

}


function render() {
    document.controls.update();
    document.planet.rotation.y += 0.0005;
    document.clouds.rotation.y += 0.0007;
    requestAnimationFrame(render);
    document.renderer.render(document.scene, document.camera);
}

function createPlanet(radius, segments, worldId) {
    return new THREE.Mesh(
        new THREE.SphereGeometry(radius, segments, segments),
        new THREE.MeshPhongMaterial({
            map:         THREE.ImageUtils.loadTexture('/worldmap.png?worldId='+worldId),
            bumpMap:     THREE.ImageUtils.loadTexture('/worldbumpmap.png?worldId='+worldId),
            bumpScale:   0.01,
            specularMap: THREE.ImageUtils.loadTexture('/worldspecularmap.png?worldId='+worldId),
            specular:    new THREE.Color(0x444444)
        })
    );
}

function createClouds(radius, segments) {
    return new THREE.Mesh(
        new THREE.SphereGeometry(radius + 0.003, segments, segments),
        new THREE.MeshPhongMaterial({
            map:         THREE.ImageUtils.loadTexture('static/images/clouds.png'),
            transparent : true,
            depthWrite  : false,
        })
    );
}

function createBackground(radius, segments) {
    return new THREE.Mesh(
        new THREE.SphereGeometry(radius, segments, segments),
        new THREE.MeshBasicMaterial({
            map:  THREE.ImageUtils.loadTexture('static/images/background.png'),
            side: THREE.BackSide
        })
    );
}

