

function generateMoon(color, diameter, orbit, speed, rotation) {

    if (document.moons == undefined){
        document.moons=[]
    }
    var sphereGeom = new THREE.SphereGeometry(diameter/2, 32, 32);
    var moonMaterial = new THREE.MeshPhongMaterial( 
            {  
                map:        THREE.ImageUtils.loadTexture('/static/images/moon.png'),
                color:      color,
            }
    );
    var moon = new THREE.Mesh(sphereGeom, moonMaterial);

    moon.rotation.y=rotation
    moon.orbit=(orbit+diameter)*2
    moon.speed=speed
    moon.visible=true
    moon.castShadow=true;
    moon.receiveShadow=true;

    document.scene.add(moon);
    document.moons.push(moon);
}


function update_moons() {
    if (document.time == undefined){
        document.time=1
    }
    document.time = document.time + 1;
    document.moons.forEach( function(moon){
        var m_angle = document.time * 0.005* moon.speed;

        moon.position.set(
          moon.orbit* Math.sin(m_angle) + document.planet.position.x, 
          0,
          moon.orbit* Math.cos(m_angle) + document.planet.position.z 
        );

    }   )

}
