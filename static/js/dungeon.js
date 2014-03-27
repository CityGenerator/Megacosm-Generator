

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

            ctx.fillStyle = "#000000";
            if (tile == 0 ){
                ctx.fillRect(c*tileSize ,r*tileSize ,tileSize, tileSize);
            }
        }
    }


}

function label_room(roomid, coords, canvas) {
    var ctx = canvas.getContext("2d");
    ctx.font=(tileSize*2)+"px Verdana";
    ctx.fillStyle='#ff0000';

    console.log(coords[0]*tileSize)
    ctx.textBaseline="middle"; 
    ctx.textAlign="center"; 

    ctx.fillText(roomid,(coords[0])*tileSize +tileSize/2,(coords[1])*tileSize+tileSize/2);

}
