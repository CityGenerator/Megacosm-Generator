//==================================================

function select_division( params){

    switch(params.division.name){
        case 'quads':
            draw_quads( params );
            break;
        case 'diagquads':
            draw_quaddiagonals( params );
            break;
        case 'diagonal':
            draw_diagonals( params );
            break;
        case 'stripes':
            draw_division_stripes( params );
            break;
        case 'none':
            draw_solid( params );
            break;
        default:
            console.log("ERROR: unknown division:"+params.division.name)
            draw_solid( params );
    }
}

//==================================================
function draw_quaddiagonals(params){
     draw_quaddiagonal( params, "north" );
     draw_quaddiagonal( params, "south" );
     draw_quaddiagonal( params, "east"  );
     draw_quaddiagonal( params, "west"  );
}

function draw_quaddiagonal(params, side, color){
    var a=0, b=0, c=0,d=0;
    if (side=="east" ){a=params.canvas.width}
    if (side=="south" ){b=params.canvas.height}
    if (side=="north" || side=="east"  ||side=="south"){c=params.canvas.width}
    if (side=="east"  || side=="south" ||side=="west" ){d=params.canvas.height}
    //console.log('quaddiag'+side)
    if (!color ){
        if (side == "north" || side == "south"){
            color=params.colors[0].hex;
        }else{
            color=params.colors[1].hex;
        }
    }
    params.flag.save();
    params.flag.beginPath();
    params.flag.moveTo(a,b);
    params.flag.lineTo(c,d);
    params.flag.lineTo(params.canvas.width/2,params.canvas.height/2);
    params.flag.fillStyle=color;
    params.flag.fill();
    params.flag.restore();

 }
//==================================================










//==================================================

function draw_solid( params){
        params.flag.fillStyle=params.colors[0].hex;
        params.flag.fillRect(0,0, params.canvas.width,params.canvas.height);
        return params.flag;

}
function draw_quads(params){

    draw_quad( params, "nw" );
    draw_quad( params, "ne" );
    draw_quad( params, "sw" );
    draw_quad( params, "se" );
}
function draw_quad(params, quadrant, color){
    var a=0,b=0,c=params.canvas.width/2, d=params.canvas.height/2;
    if (quadrant == "ne" || quadrant == "se" ){
        a=params.canvas.width/2;
    }
    if (quadrant == "se" || quadrant == "sw" ){
        b=params.canvas.height/2;
    }

    if ( color == undefined) {
        if (quadrant == "nw" || quadrant == "se" ){
            color=params.colors[0].hex;
        }else{
            color=params.colors[1].hex;
        }
    }


    params.flag.fillStyle=color;

    params.flag.fillRect( a, b, c, d );
}
//==================================================


function draw_division_stripes(params){
    for (var i=0; i<=params.division_stripes_count; i++){
        draw_stripe(params, params.division_stripes_side, params.division_stripes_count, i);
    }
}


function draw_stripe(params, side, count, id,color){

    if (! color){
        var colorid=id % params.division_stripes_colorcount;
        color=params.colors[colorid].hex;
    }
    params.flag.fillStyle=color;

    if (side=="horizontal"){
        var thickness=Math.floor(params.canvas.height/count);
        params.flag.fillRect(0, (thickness*id)   ,params.canvas.width,thickness);

    }else {
        var thickness=Math.floor(params.canvas.width/count);
        params.flag.fillRect( (thickness*id),0 ,thickness  ,params.canvas.height);
    }
}








//==================================================
function draw_diagonal(params, side, color ){
    var start,mid,end;
    console.log(params.division_diagonal_direction)
    if (side == "north" && params.division_diagonal_direction == "left-to-right"){
        start=[0,0];
        mid=[params.canvas.width,0];
        end=[params.canvas.width,params.canvas.height];

    }else if (side == "south" && params.division_diagonal_direction == "left-to-right"){
        start=[0,0];
        mid=[0,params.canvas.height];
        end=[params.canvas.width,params.canvas.height];

    }else if (side == "north" && params.division_diagonal_direction == "right-to-left"){
        start=[params.canvas.width,0];
        mid=[0,0];
        end=[0,params.canvas.height];

    }else if (side == "south" && params.division_diagonal_direction == "right-to-left"){
        start=[params.canvas.width,0];
        mid=[params.canvas.width,params.canvas.height];
        end=[0,params.canvas.height];
    }
    if (! color){
        if (side == "north"){
            color=params.colors[0].hex;
        }else{
            color=params.colors[1].hex;
        }
    }

    params.flag.save();
    params.flag.beginPath();
    params.flag.moveTo(start[0],start[1]);
    params.flag.lineTo(mid[0],mid[1]);
    params.flag.lineTo(end[0],end[1]);
    params.flag.fillStyle=color;
    params.flag.fill();
    params.flag.restore();
}


function draw_diagonals(params ){

    draw_diagonal(params, "north") ;
    draw_diagonal(params, "south") ;
}

