

var tileSize = 8;       // The size of a tile (32×32)


function create_dungeon(jsonblock,canvas) {
    canvas.width = tileSize*jsonblock[0].length
    canvas.height= tileSize*jsonblock.length
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#A88442";
    ctx.fillRect(0,0,jsonblock[0].length*tileSize, jsonblock.length*tileSize);


    for (var r = 0; r < jsonblock.length ; r++) {
        for (var c = 0; c < jsonblock[r].length; c++) {
            var tile = jsonblock[ r ][ c ] ;
            if (tile.class == 'tile' ){
                ctx.fillStyle = "#000000";
                ctx.fillRect(c*tileSize ,r*tileSize ,tileSize, tileSize);
            }else if (tile.class == 'halltile' ){
                ctx.fillStyle = "rgba(0,0,0,0.3)";
                ctx.fillRect(c*tileSize ,r*tileSize ,tileSize, tileSize);
            }


        }
    }
    for (var r = 0; r < jsonblock.length ; r++) {
        for (var c = 0; c < jsonblock[r].length; c++) {
            var tile = jsonblock[ r ][ c ] ;
            if (tile.doorway == 1 ){
                ctx.fillStyle = "rgba(0,255,0,0.3)";
                ctx.fillRect(c*tileSize ,r*tileSize ,tileSize, tileSize);
            }
        }
    }

}



function label_room(roomid, coords, canvas) {
    var ctx = canvas.getContext("2d");
    ctx.font=(tileSize*2)+"px Verdana";
    ctx.fillStyle='#ffffff';

    console.log(coords[0]*tileSize)
    ctx.textBaseline="middle"; 
    ctx.textAlign="center"; 

    ctx.fillText(roomid,(coords[0])*tileSize +tileSize/2,(coords[1])*tileSize+tileSize/2);

}




var geomorphTileSize = 100;


function create_geomorphdungeon(jsonblock,canvas) {

    canvas.width = geomorphTileSize * jsonblock[0].length;
    canvas.height = geomorphTileSize * jsonblock.length;
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#A88442";
    ctx.fillRect(0, 0, jsonblock[0].length * geomorphTileSize, jsonblock.length * geomorphTileSize);
    
    for (var y = 0; y < jsonblock.length; y++) {
        for (var x = 0; x < jsonblock[y].length; x++) {
            var tiledata = jsonblock[y][x];
            var newtile = new Image();
            newtile.src = tiledata.path;
            newtile.onload = drawTile(canvas, x, y, newtile, tiledata.rotation);
        }
    }
}


function drawTile(canvas, x, y, tile, rotation) {
    var TO_RADIANS = Math.PI / 180;
    var ctx = canvas.getContext("2d");
    ctx.save();

    var degrees = 90 * rotation;
    ctx.translate( x*geomorphTileSize+geomorphTileSize/2, y*geomorphTileSize+ geomorphTileSize/2 );
    ctx.rotate( degrees*TO_RADIANS );
    ctx.translate(  -(x*geomorphTileSize+geomorphTileSize/2), -(y*geomorphTileSize+ geomorphTileSize/2));
    ctx.drawImage(tile, x*geomorphTileSize, y*geomorphTileSize);

    ctx.restore();

    //This is where we want the pivot point; it should stay in the center of the black box.    
    ctx.rect(x * geomorphTileSize + geomorphTileSize / 2, y * geomorphTileSize + geomorphTileSize / 2, 2, 2);
    ctx.fillStyle = "red";
    ctx.fill();
    

}






