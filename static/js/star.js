
function generate_stars(worldId){
    //A little ambient light to see stuff on the back side.
    document.scene.add(new THREE.AmbientLight(0x222222));


    document.star=[]
    document.starGlow=[]
    document.light=[]
    var halo=1.5
    var diameter=1
    var intensity=0.6
    var rotation=worldId



    // Lets replicate the light of a single star to start with.
    var color= 0x99ffff
    var diameter=.5
    var halo=2
    var intensity=1
    var position= new THREE.Vector3( 0,0, -10 );
    
    generateStar(color, position, diameter, intensity, halo, rotation);

//    var color= 0xffff00
//    var diameter=1
//    var halo=1.5
//    var intensity=0.6
//    var position= new THREE.Vector3( 17, 3, -40 );
//    //var position= new THREE.Vector3( 6,2, -10 );
//    
//    generateStar(color, position, diameter, intensity, halo,rotation);
//
//
//    var halo=1.5
//    var diameter=4
//    var intensity=0.01
//    var color= 0xff0000
//    var position= new THREE.Vector3( 24, -2, -50 );
//    //var position= new THREE.Vector3( 6,2, -10 );
//    
//    generateStar(color, position, diameter, intensity, halo,rotation);

}




function generateStar(color, position, diameter, intensity, halo, rotation) {

    var sphereGeom = new THREE.SphereGeometry(diameter, 32, 32);
    var starMaterial = new THREE.MeshPhongMaterial( 
            {  
                map:        THREE.ImageUtils.loadTexture('/static/images/star.png'),
                emissive:   color,
            }
    );
    var star = new THREE.Mesh(sphereGeom, starMaterial);

    star.position=position;
    star.rotation.y=rotation
    star.visible=true
    document.scene.add(star);
    document.star.push(star);

    this.starGlow = new THREE.Mesh( new THREE.SphereGeometry(diameter, 32, 32)   , Create_Shader_Material(color) );
    starGlow.position = position
    starGlow.material.side = THREE.BackSide; 
    starGlow.scale.multiplyScalar(halo);
    document.scene.add( starGlow );
    document.starGlow.push(starGlow);

    var light = new THREE.PointLight(color, intensity, 10000);
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

