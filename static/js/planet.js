
function generate_planet(seed, size){
    // planet params
        segments = 30;

    // We need to create two parts,
    document.planet = createPlanet(size, segments, seed);
    document.planet.rotation.y = 0;
    
    document.planet.castShadow=true;
    document.planet.receiveShadow=true;

    document.scene.add(document.planet)

    document.clouds = createClouds(size*1.01, segments);
    document.clouds.rotation.y = 0;
    document.clouds.castShadow=true;
    document.clouds.receiveShadow=true;
//    document.scene.add(document.clouds)

}

function createPlanet(radius, segments, seed) {

    texture = THREE.ImageUtils.loadTexture('/static/images/samplecontinent.png')
    texture.offset=new Vector(0.3,1.4)
    return new THREE.Mesh(
        new THREE.SphereGeometry(radius, segments, segments),
        new THREE.MeshPhongMaterial({
            color:      0x0000ff,
              map:         texture,
//            bumpMap:     THREE.ImageUtils.loadTexture('/worldbumpmap.png?seed='+seed),
//            bumpScale:   0.05,
//            specularMap: THREE.ImageUtils.loadTexture('/worldspecularmap.png?seed='+seed),
//            specular:    new THREE.Color(0x222222)
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

