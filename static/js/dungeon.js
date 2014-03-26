

function create_dungeon(jsonblock,canvas) {


    var tilesetImage = new Image();
    tilesetImage.src = "/static/images/dungeon/minitiles.png";
    tilesetImage.onload = drawImage;
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#A88442";
    var tileSize = 20;       // The size of a tile (32×32)
    ctx.fillRect(0,0,jsonblock[0].length*tileSize, jsonblock.length*tileSize);
    var imageNumTiles = 4;  // The number of tiles per row in the tileset image

    function drawImage () {
        for (var r = 0; r < jsonblock.length ; r++) {
            for (var c = 0; c < jsonblock[r].length; c++) {
                var tile = parseInt( jsonblock[ r ][ c ],2) ;

                console.log(tile);
                var tileRow = (tile / imageNumTiles) | 0; // Bitwise OR operation
                var tileCol = (tile % imageNumTiles) | 0;
                ctx.drawImage(tilesetImage, (tileCol * tileSize), (tileRow * tileSize), tileSize, tileSize, (c * tileSize), (r * tileSize), tileSize, tileSize);
            }
        }
    }


}
