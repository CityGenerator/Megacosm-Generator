

function create_dungeon(jsonblock,canvas) {
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#A88442";
    var tileSize = 10;       // The size of a tile (32×32)
    ctx.fillRect(0,0,jsonblock[0].length*tileSize, jsonblock.length*tileSize);
    var imageNumTiles = 4;  // The number of tiles per row in the tileset image

    for (var r = 0; r < jsonblock.length ; r++) {
        for (var c = 0; c < jsonblock[r].length; c++) {
            var tile = jsonblock[ r ][ c ] ;

            ctx.fillStyle = "#000000";
            if (tile == 0 ){
                ctx.fillRect(c*tileSize ,r*tileSize ,tileSize, tileSize);
            }
        }
    }


}

function label_room(roomid, coords, canvas) {
    var ctx = canvas.getContext("2d");
    ctx.font="20px Verdana";
    ctx.fillStyle='#ff0000';

    var tileSize = 10;       // The size of a tile (32×32)
    console.log(coords[0]*tileSize)
    ctx.textBaseline="middle"; 
    ctx.textAlign="center"; 

    ctx.fillText(roomid,(coords[0])*tileSize +5,(coords[1])*tileSize+5);

}
