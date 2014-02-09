
function generate_planet(worldId){
    // planet params
    var radius   = 0.5,
        segments = 30;

    // We need to create two parts,
    document.planet = createPlanet(radius, segments, worldId);
    document.planet.rotation.y = 0;
    document.planet.castShadow=true;
    document.planet.receiveShadow=true;

    document.scene.add(document.planet)

    document.clouds = createClouds(radius+0.01, segments);
    document.clouds.rotation.y = 0;
    document.clouds.castShadow=true;
    document.clouds.receiveShadow=true;
    document.scene.add(document.clouds)

}

function createPlanet(radius, segments, worldId) {
    return new THREE.Mesh(
        new THREE.SphereGeometry(radius, segments, segments),
        new THREE.MeshPhongMaterial({
            map:         THREE.ImageUtils.loadTexture('/worldmap.png?worldId='+worldId),
            bumpMap:     THREE.ImageUtils.loadTexture('/worldbumpmap.png?worldId='+worldId),
            bumpScale:   0.01,
            specularMap: THREE.ImageUtils.loadTexture('/worldspecularmap.png?worldId='+worldId),
            specular:    new THREE.Color(0x222222)
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

