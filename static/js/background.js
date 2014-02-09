
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
    document.camera.position.z = -3.5;
    // And a renderer
    document.renderer = new THREE.WebGLRenderer( {antialias:true} );

    document.renderer.setSize(WIDTH, HEIGHT);

    //Then lets throw a background up for flavor
    background = createBackground(90, 64);
    document.scene.add(background);


    // Add the control features
    document.controls = new THREE.TrackballControls(document.camera);

    // add our new renderer to our div
    planetwindow.appendChild(document.renderer.domElement);
}



function render() {
    document.renderer.render(document.scene, document.camera);

}

function animate() 
{
    requestAnimationFrame( animate );
    render();
    update();
}
time=1
function update()
{
    document.controls.update();

    if ( document.planet){
        document.planet.rotation.y += 0.0005;
    }
    if ( document.clouds){
        document.clouds.rotation.y += 0.0007;
    }

    if ( document.starGlow){
        document.starGlow.forEach( function(glow){
            glow.material.uniforms.viewVector.value = 
                new THREE.Vector3().subVectors( document.camera.position, glow.position );
        }   )
    }
    speed=0.2
    time = time + speed;
    var m_angle = time * 0.01;

    if ( document.moons){
        document.moons.forEach( function(moon){
            moon.position.set(
              1* Math.sin(m_angle) + document.planet.position.x, 
              0,
              1* Math.cos(m_angle) + document.planet.position.z 
            );

        }   )
    }




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

