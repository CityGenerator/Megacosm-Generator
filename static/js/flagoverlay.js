// overlay should use colors 3
function select_overlay( params ){
    var color=params.colors[3].hex;
    console.log("overlay: "+params.overlay['name'])
    switch(params.overlay['name']){
            case 'stripe':
                draw_stripe(params, params['overlay_stripe_side'], params['overlay_stripe_count'],params['overlay_stripe_countselected'], color);
                break;
            case 'quaddiag':
                draw_quaddiagonal(params, params['overlay_quaddiag_side'], color);
                break;
            case 'quad':
                draw_quad(params, params['overlay_quad_side'], color);
                break;
            case 'diamond':
                draw_overlay_diamond(params); //TODO pass in 2 colors so it can be used as a symbol
                break;
            case 'circle':
                draw_overlay_circle(params );
                break;
            case  'rays':
                draw_overlay_rays( params );
                break;
            case 'cross':
                draw_overlay_cross(params);
                break;
            case 'slash':
                draw_slash(params);
                break;
            case 'x':
                draw_slash(params,'left-to-right');
                draw_slash(params,'right-to-left');
                break;
// FIXME both jack and asterisk need to be rewritten
//            case 'jack':
//                draw_slash(params,'left-to-right');
//                draw_slash(params,'right-to-left');
//                draw_overlay_cross(params);
//                break;
    }
}












function draw_overlay_diamond(params){
    params.flag.save();
    params.flag.beginPath();
    params.flag.moveTo(    params.canvas.width/2,  0  );
    params.flag.lineTo(    params.canvas.width,    params.canvas.height/2 );
    params.flag.lineTo(    params.canvas.width/2,  params.canvas.height );
    params.flag.lineTo(    0,                      params.canvas.height/2 );
    params.flag.fillStyle=params.colors[3].hex;
    params.flag.fill();
    params.flag.restore();
    if (params.overlay.outline=="false"){
        params.flag.save();
        params.flag.beginPath();
        params.flag.lineWidth=10;
        params.flag.moveTo(    params.canvas.width/2,  0  );
        params.flag.lineTo(    params.canvas.width,    params.canvas.height/2 );
        params.flag.lineTo(    params.canvas.width/2,  params.canvas.height );
        params.flag.lineTo(    0,                      params.canvas.height/2 );
        params.flag.lineTo(    params.canvas.width/2,  0  );
        params.flag.strokeStyle=params.colors[4].hex;
        params.flag.stroke();
        params.flag.restore();
    }

}


function draw_overlay_circle(params){

    var radius;
    if (params.overlay_circle_radiusdirection =="horizontal"){
        radius=params.overlay_circle_radius*params.canvas.width
    }else{
        radius=params.overlay_circle_radius*params.canvas.height
    }
    var width=params.canvas.width*params.overlay_circle_x
    var height=params.canvas.height*params.overlay_circle_y
    params.flag.save()
    params.flag.beginPath(); // Start the path
    params.flag.arc(width,height, radius, 0, Math.PI*2, false ); // Draw a circle
    params.flag.closePath(); // Close the path
    params.flag.fillStyle=params.colors[3].hex;
    params.flag.fill(); // Fill the path
    params.flag.restore();

    if (params.overlay_circle_outline =="true"){
        params.flag.save()
        params.flag.beginPath(); // Start the path
        params.flag.lineWidth=params.overlay_circle_outlinewidth;
        params.flag.arc(width,height, radius, 0, Math.PI*2, false ); // Draw a circle
        params.flag.closePath(); // Close the path
        params.flag.strokeStyle=params.colors[4].hex;
        params.flag.stroke(); // Fill the path
        params.flag.restore();
    }

}


function draw_overlay_rays(params){

    var count=params.overlay_rays_count;
    var angle=360/count;
    var x=params.canvas.width *params.overlay_rays_x
    var y=params.canvas.height*params.overlay_rays_y
    x=params.canvas.width/2;
    y=params.canvas.height/2;
    var offset=params.overlay_rays_offset;
    params.flag.save();
    params.flag.fillStyle=params.colors[3].hex;
    params.flag.translate(x,y);
    while (count-- >0){
        params.flag.beginPath();
        params.flag.moveTo(0,-offset*params.canvas.width/2);
        params.flag.lineTo(0,-params.canvas.width*2.5);
        params.flag.rotate(angle/2 * Math.PI/180);
        params.flag.lineTo(0,-params.canvas.width*2.5);
        params.flag.lineTo(0,-offset*params.canvaswidth/2);

        params.flag.closePath();
        params.flag.fill();
        params.flag.rotate(angle/2 * Math.PI/180);
    }
    params.flag.translate(-x,-y);
    params.flag.restore();
}


function draw_overlay_cross(params){
    draw_vertical_crossbar(params);
    draw_horizontal_crossbar(params);
}

function draw_vertical_crossbar(params){
    var width=params.canvas.width*params.overlay_cross_vertwidth;
    var length=params.canvas.width*params.overlay_cross_vertlength;

    var startx=params.canvas.width/2 - width/2;
    var starty= (params.canvas.height-length)/2
    params.flag.fillStyle=params.colors[3].hex;

    params.flag.fillRect( startx, starty, width,  length );
}

function draw_horizontal_crossbar(params){

    var width=params.canvas.height*params.overlay_cross_horwidth;
    var length=params.canvas.width*params.overlay_cross_horlength;
    var startx=(params.canvas.width-length)/2 ;
    var starty=params.canvas.height*params.overlay_cross_horpos - width/2
    params.flag.fillStyle=params.colors[3].hex;
    params.flag.fillRect( startx, starty,length,width);

}






function draw_slash(params, direction){

    params.flag.beginPath();

    if (! direction){
        direction = params.overlay_slash_direction
    }


    var linewidth=params.canvas.width * params.overlay_slash_width;
    var lineheight=params.canvas.height * params.overlay_slash_width;
    if (direction =='left-to-right'){
        params.flag.moveTo(    0,                               0);
        params.flag.lineTo(    linewidth,                       0);
        params.flag.lineTo(    params.canvas.width,             params.canvas.height-lineheight);
        params.flag.lineTo(    params.canvas.width,             params.canvas.height);
        params.flag.lineTo(    params.canvas.width-linewidth,   params.canvas.height);
        params.flag.lineTo(    0,                               lineheight);
    }else{
        params.flag.moveTo(    params.canvas.width-linewidth,   0);
        params.flag.lineTo(    params.canvas.width,             0);
        params.flag.lineTo(    params.canvas.width,             lineheight);
        params.flag.lineTo(    linewidth,                       params.canvas.height);
        params.flag.lineTo(    0,                               params.canvas.height);
        params.flag.lineTo(    0,                               params.canvas.height-lineheight);
    }
    params.flag.fillStyle=params.colors[3].hex;
    params.flag.fill();
}

