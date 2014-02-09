
function generate_moons(seed){
    //A little ambient light to see stuff on the back side.

    document.moons=[]

    var rotation=seed

    var color= 0xff9999
    var diameter=.1
    var position= new THREE.Vector3( 0 ,0, -2 );
    
    generateMoon(color, position, diameter, rotation);

}

function generateMoon(color, position, diameter, rotation) {

    var sphereGeom = new THREE.SphereGeometry(diameter, 32, 32);
    var moonMaterial = new THREE.MeshPhongMaterial( 
            {  
                map:        THREE.ImageUtils.loadTexture('/static/images/moon.png'),
                color:      color,
            }
    );
    var moon = new THREE.Mesh(sphereGeom, moonMaterial);

    moon.position=position;
    moon.rotation.y=rotation
    moon.visible=true
    moon.castShadow=true;
    moon.receiveShadow=true;

    document.scene.add(moon);
    document.moons.push(moon);
}

