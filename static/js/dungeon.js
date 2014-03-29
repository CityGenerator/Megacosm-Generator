

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
    canvas.width = geomorphTileSize*jsonblock[0].length
    canvas.height= geomorphTileSize*jsonblock.length
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#A88442";
    ctx.fillRect(0,0,jsonblock[0].length*geomorphTileSize, jsonblock.length*geomorphTileSize);

    var TO_RADIANS = Math.PI/180; 

    for (var y = 0; y < jsonblock.length ; y++) {
        for (var x = 0; x < jsonblock[y].length; x++) {


            var tiledata = jsonblock[ y ][ x ] ;
            ctx.save();
            var newtile = new Image();
            console.log(tiledata.path);
            newtile.src = tiledata.path;
            //ctx.rotate((90*tiledata.rotation) * TO_RADIANS );
            console.log("rotate "+ ( 90*tiledata.rotation  )+" degrees")
            newtile.onload = function() {
                console.log(x)
                ctx.drawImage(newtile, x*geomorphTileSize, y*geomorphTileSize);
            };
            ctx.restore();


        }
    }

}
