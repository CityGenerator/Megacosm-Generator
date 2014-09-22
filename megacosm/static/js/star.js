
function generateStar(color, position, diameter, intensity, halo, rotation) {
    if (document.star == undefined){
        document.star=[]
    }
    if (document.starGlow == undefined){
        document.starGlow=[]
    }
    if (document.light == undefined){
        document.light=[]
    }
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

    this.starGlow = new THREE.Mesh( new THREE.SphereGeometry(diameter+0.5, 32, 32)   , Create_Shader_Material(color) );
    starGlow.position = position
    starGlow.material.side = THREE.BackSide; 
    starGlow.scale.multiplyScalar(halo);
    document.scene.add( starGlow );
    document.starGlow.push(starGlow);

    var light = new THREE.DirectionalLight(color, intensity, 1);
    light.castShadow=true;
    light.position= position;
    //light.shadowCameraVisible = true;  //debugging box

    light.shadowCameraNear = 10;
    light.shadowCameraFar = 20-star.position.x

    light.shadowDarkness = 0.5;
    light.shadowCameraLeft = -2.5;
    light.shadowCameraRight = 2.5;
    light.shadowCameraTop = 2.5;
    light.shadowCameraBottom = -2.5;

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

