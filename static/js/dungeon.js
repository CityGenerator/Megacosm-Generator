

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

//#############################################################################################3


var geomorphTileSize = 200;


function create_geomorphdungeon(jsonblock,canvas, bgimage) {

    canvas.width = geomorphTileSize * jsonblock[0].length;
    canvas.height = geomorphTileSize * jsonblock.length;
   
    var img = new Image();
    img.src = "/static/images/backgrounds/"+bgimage+".png";
    img.onload = function(){
        var ctx = canvas.getContext("2d");
        var ptrn = ctx.createPattern(img, 'repeat'); // Create a pattern with this image, and set it to "repeat".
        ctx.fillStyle = ptrn;
        ctx.fillRect(0, 0, canvas.width, canvas.height); // ctxbg.fillRect(x, y, width, height);
        draw_grid(canvas,20);
        load_geomorphtiles(jsonblock, canvas)
    }
}

function load_geomorphtiles(jsonblock, canvas){

    for (var y = 0; y < jsonblock.length; y++) {
        for (var x = 0; x < jsonblock[y].length; x++) {
            var geomorphx=x*geomorphTileSize;
            var geomorphy=y*geomorphTileSize;

            var tiledata = jsonblock[y][x];

            function drawTile( geox, geoy, tiledata, canvas) {

                var newtile = new Image();
                newtile.onload = function(){
                    var ctx = canvas.getContext("2d");
                    ctx.save();
                    var degrees = 90 * tiledata.rotation;
                    ctx.translate( geox+geomorphTileSize/2, geoy+ geomorphTileSize/2 );
                    var TO_RADIANS = Math.PI / 180;
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
            drawTile(geomorphx, geomorphy, tiledata, canvas)

        }
    }
}
function draw_grid(canvas, width){

    var ctx=canvas.getContext("2d");
    ctx.save();
    ctx.lineWidth = 1;
    for (var x = 0; x < canvas.width; x+=width) {
            ctx.beginPath();
            ctx.strokeStyle = "rgba(128,128,128,1)";
            ctx.moveTo(x,0);
            ctx.lineTo(x,canvas.height);
            ctx.stroke();

    }
    // horizontal lines
    for (var y = 0; y < canvas.height; y+=width) {
            ctx.beginPath();
            ctx.strokeStyle = "rgba(128,128,128,1)";
            ctx.moveTo(0,y);
            ctx.lineTo(canvas.width,y);
            ctx.stroke();

    }
    for (var x = 0; x < canvas.width; x+=width) {

            ctx.beginPath();
            ctx.strokeStyle = "rgba(0,0,0,0.5)";
            ctx.moveTo(x-1,0);
            ctx.lineTo(x-1,canvas.height);
            ctx.stroke();
    }
    // horizontal lines
    for (var y = 0; y < canvas.height; y+=width) {

            ctx.beginPath();
            ctx.strokeStyle = "rgba(0,0,0,0.5)";
            ctx.moveTo(0,y-1);
            ctx.lineTo(canvas.width,y-1);
            ctx.stroke();
    }


    ctx.restore();
}

