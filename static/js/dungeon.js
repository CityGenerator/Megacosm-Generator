

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




var geomorphTileSize = 200;

var TO_RADIANS = Math.PI / 180;

function create_geomorphdungeon(jsonblock,canvas,canvasbg, bgimage) {

    canvas.width = geomorphTileSize * jsonblock[0].length;
    canvas.height = geomorphTileSize * jsonblock.length;
    var ctx = canvas.getContext("2d");
//    ctx.fillStyle = "#A88442";
//    ctx.fillRect(0, 0, jsonblock[0].length * geomorphTileSize, jsonblock.length * geomorphTileSize);
   


    var ctxbg = canvasbg.getContext("2d");
    canvasbg.width = geomorphTileSize * jsonblock[0].length;
    canvasbg.height = geomorphTileSize * jsonblock.length;
    var img = new Image();
    img.src = "/static/images/backgrounds/"+bgimage+".png";
    img.onload = function(){
        // create pattern
        var ptrn = ctxbg.createPattern(img, 'repeat'); // Create a pattern with this image, and set it to "repeat".
        ctxbg.fillStyle = ptrn;
        ctxbg.fillRect(0, 0, canvas.width, canvas.height); // ctxbg.fillRect(x, y, width, height);
    }



 
    for (var y = 0; y < jsonblock.length; y++) {
        for (var x = 0; x < jsonblock[y].length; x++) {
            var geomorphx=x*geomorphTileSize;
            var geomorphy=y*geomorphTileSize;

            var tiledata = jsonblock[y][x];

            drawTile(geomorphx, geomorphy, tiledata, canvas)
            function drawTile( geomorphx, geomorphy, tiledata, canvas) {


                var newtile = new Image();
                newtile.onload = function(){
                    var ctx = canvas.getContext("2d");
                    var geox=geomorphx
                    var geoy=geomorphy
                    ctx.save();
                    var degrees = 90 * tiledata.rotation;
                    ctx.translate( geox+geomorphTileSize/2, geoy+ geomorphTileSize/2 );
                    ctx.rotate( degrees*TO_RADIANS );
                    ctx.translate(  -( geox+geomorphTileSize/2), -(geoy+ geomorphTileSize/2));
                    ctx.drawImage(newtile, geox, geoy);
                    ctx.restore();
    
                    ctx.rect( geox + geomorphTileSize / 2, geoy  + geomorphTileSize / 2, 2, 2);
                    ctx.fillStyle = "red";
                    ctx.fill();
                }
            newtile.src = tiledata.path;
            }

        }
    }
}








