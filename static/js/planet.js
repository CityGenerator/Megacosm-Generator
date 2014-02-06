
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



function generate_stars(worldId){
    //A little ambient light to see stuff on the back side.
    document.scene.add(new THREE.AmbientLight(0x444444));


    document.star=[]
    document.starGlow=[]
    document.light=[]
    var halo=1.5
    var diameter=0.25
    var intensity=0.6




    // Lets replicate the light of a single star to start with.
    var color= 0x99ffff
    var position= new THREE.Vector3( 0,0, 0 );
    //var position= new THREE.Vector3( 5,1, -10 );
    
    generateStar(color, position, diameter, intensity, halo);

    var color= 0xffff00
    var position= new THREE.Vector3( 3, 2, -5 );
    //var position= new THREE.Vector3( 6,2, -10 );
    
    generateStar(color, position, diameter, intensity, halo);

}




function generateStar(color, position, diameter, intensity, halo) {

    var sphereGeom = new THREE.SphereGeometry(diameter, 32, 32);
    var starMaterial = new THREE.MeshPhongMaterial( 
          {  
                map:         THREE.ImageUtils.loadTexture('/static/images/star.png'),
                emissive:color,
            }
    );
    var star = new THREE.Mesh(sphereGeom, starMaterial);

    star.position=position;
    star.visible=true
    document.scene.add(star);
    document.star.push(star);

    this.starGlow = new THREE.Mesh( new THREE.SphereGeometry(diameter, 32, 32)   , Create_Shader_Material(color) );
    starGlow.position = position
    starGlow.material.side = THREE.BackSide; 
    starGlow.scale.multiplyScalar(halo);
    document.scene.add( starGlow );
    document.starGlow.push(starGlow);

    var light = new THREE.DirectionalLight(color, intensity);
    light.position= position;
    document.scene.add(light);
    document.light.push(light);


}



function Create_Shader_Material(color){
    return new THREE.ShaderMaterial({
        uniforms: 
        { 
            "c":   { type: "f", value: 0.1},
            "p":   { type: "f", value: 3},
            glowColor: { type: "c", value: new THREE.Color(color) },
            viewVector: { type: "v3", value: document.camera.position }
        },
        vertexShader:   document.getElementById( 'vertexShader'   ).textContent,
        fragmentShader: document.getElementById( 'fragmentShader' ).textContent,
        side: THREE.DoubleSide,
        blending: THREE.AdditiveBlending,
        transparent: true
    }   );
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

    document.planet.visible=false
    document.clouds.visible=false
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

function update()
{
    document.controls.update();

    document.planet.rotation.y += 0.0005;
    document.clouds.rotation.y += 0.0007;

    document.starGlow.forEach( function(glow){
        glow.material.uniforms.viewVector.value = 
            new THREE.Vector3().subVectors( document.camera.position, glow.position );
    }   )

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

