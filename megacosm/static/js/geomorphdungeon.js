 //#############################################################################################3

function save_as_png(canvasname){
    var canvas=document.getElementById(canvasname);
    window.location = canvas.toDataURL("image/png");

}



var geomorphTileSize = 200;


function create_geomorphdungeon(jsonblock,canvas, bgimage, decoration, decoration_offset) {

    canvas.width = geomorphTileSize * jsonblock[0].length;
    canvas.height = geomorphTileSize * jsonblock.length;
   
    var img = new Image();
    img.src = "/static/images/backgrounds/"+bgimage+".png";
    img.onload = function(){
        var ctx = canvas.getContext("2d");
        var ptrn = ctx.createPattern(img, 'repeat'); // Create a pattern with this image, and set it to "repeat".
        ctx.fillStyle = ptrn;
        ctx.fillRect(0, 0, canvas.width, canvas.height); // ctxbg.fillRect(x, y, width, height);
        draw_decoration(jsonblock, canvas, decoration, decoration_offset  )

    }
}


function draw_decoration(jsonblock,canvas, decoration, dec_offset) {
   
    var img = new Image();

    if (decoration != "" ){
        img.src = "/static/images/decorations/"+decoration+".png";
        img.onload = function(){
            var ctx = canvas.getContext("2d");
            var offsetx=dec_offset*canvas.width;
            var offsety=dec_offset*canvas.height;
            ctx.translate(-offsetx,-offsety);

            var ptrn = ctx.createPattern(img, 'repeat'); // Create a pattern with this image, and set it to "repeat".
            ctx.fillStyle = ptrn;


            ctx.fillRect(offsetx,offsety, canvas.width, canvas.height); // ctxbg.fillRect(x, y, width, height);
            ctx.translate(offsetx,offsety);


            draw_grid(canvas,20);
    
            load_geomorphtiles(jsonblock, canvas)
        }
    }else{
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
    
                    //ctx.rect( geox + geomorphTileSize / 2, geoy  + geomorphTileSize / 2, 2, 2);
                    //ctx.fillStyle = "red";
                    //ctx.fill();
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

