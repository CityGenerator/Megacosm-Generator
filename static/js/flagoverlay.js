
var flag_gen = flag_gen||{};

// these objects keep the functions organized
flag_gen.draw_overlay=flag_gen.draw_overlay||{};
flag_gen.overlay_utils=flag_gen.overlay_utils||{};


flag_gen.select_overlay = function( flag, overlay_params, colors, canvas_width, canvas_height ){   console.log("overlay: "+overlay_params.name)
    var draw_overlay = flag_gen.draw_overlay,
        overlay_type = overlay_params.name;
    
    draw_overlay[overlay_type](flag, overlay_params[overlay_type], colors, canvas_width, canvas_height);
    //TODO: Add 'jack' and 'asterisk' types (they are built from slashes adn crosses)
};

flag_gen.overlay_utils.finish_shape = function(flag, color) {
    flag.fillStyle = color;
    flag.fill();
    //flag.restore();
};
flag_gen.overlay_utils.finish_outline = function(flag, color, thickness) {
    flag.lineWidth = thickness;
    flag.strokeStyle = color;
    flag.stroke();
    flag.restore();
};


// Quad
flag_gen.draw_overlay.quad = function(flag, quad_params, colors, canvas_width, canvas_height) {//todo: share with flagdivision
    var points = flag_gen.utils.get_quad_points(quad_params.side, canvas_width, canvas_height);
    
    flag.fillStyle = colors[3].hex;
    flag.fillRect(points[0][0], points[0][1], points[1][0], points[1][1]);
};


// Quaddiagonal
flag_gen.draw_overlay.quaddiag = function(flag, quaddiagonal_params, colors, canvas_width, canvas_height) {
    
    var points = flag_gen.utils.get_quaddiag_points(quaddiagonal_params.side, canvas_width, canvas_height);
    
    flag.save();
    flag.beginPath();
    flag.moveTo(points[0][0], points[0][1]);
    flag.lineTo(points[1][0], points[1][1]);
    flag.lineTo(points[2][0], points[2][1]);
    flag_gen.overlay_utils.finish_shape(flag, colors[3].hex);
    
};


// Stripe
flag_gen.draw_overlay.stripe = function(flag, stripe_params, colors, canvas_width, canvas_height) {
    var thickness = 0,
        start = 0;
    
    flag.fillStyle=colors[3].hex;
    if (stripe_params.side==='horizontal') {
        thickness = Math.floor(canvas_height/stripe_params.count);
        start = thickness * stripe_params.countselected;
        flag.fillRect(0, start, canvas_width, thickness);
    }
    else {
        thickness = Math.floor(canvas_width/stripe_params.count);
        start = thickness * stripe_params.countselected;
        flag.fillRect(start, 0, thickness, canvas_height);
    }
};


// Cross
flag_gen.draw_overlay.cross = function(flag, cross_params, colors, canvas_width, canvas_height){
    var utils = flag_gen.overlay_utils,
        color = colors[3].hex;
    utils.draw_crossbar_vertical(flag, cross_params.vertwidth, cross_params.vertlength,color,  canvas_width, canvas_height);
    utils.draw_crossbar_horizontal(flag, cross_params.horwidth, cross_params.horlength, cross_params.horpos, color, canvas_width, canvas_height);
};
flag_gen.overlay_utils.draw_crossbar_vertical = function(flag, vwidth, vlength, color, canvas_width, canvas_height){
    var width=canvas_width*vwidth,
        length=canvas_width*vlength,
        startx=canvas_width/2 - width/2,
        starty= (canvas_height-length)/2;
    flag.fillStyle=color;
    flag.fillRect( startx, starty, width,  length );
};
flag_gen.overlay_utils.draw_crossbar_horizontal = function(flag, hwidth, hlength, hpos, color, canvas_width, canvas_height){
    var width=canvas_height*hwidth,
        length=canvas_width*hlength,
        startx=(canvas_width-length)/2,
        starty=canvas_height*hpos - width/2;
    flag.fillStyle=color;
    flag.fillRect( startx, starty,length,width);
};


// Diamond
flag_gen.draw_overlay.diamond = function(flag, diamond_params, colors, canvas_width, canvas_height) {
    var utils = flag_gen.overlay_utils;
    
    utils.draw_diamond(flag, canvas_width, canvas_height);
    utils.finish_shape(flag, colors[3].hex);
    
    if (diamond_params.outline==="false"){
        utils.draw_diamond(flag, canvas_width, canvas_height);
        utils.finish_outline(flag, colors[4].hex, 10);
    }
};
flag_gen.overlay_utils.draw_diamond = function(flag, width, height) {
    var half_width = width/2,
        half_height = height/2;
    
    flag.save();
    flag.beginPath();
    flag.moveTo(    half_width,     0  );
    flag.lineTo(    width,          half_height );
    flag.lineTo(    half_width,     height );
    flag.lineTo(    0,              half_height );
    flag.lineTo(    half_width,     0  );
};



// Circle
flag_gen.draw_overlay.circle = function(flag, circle_params, colors, canvas_width, canvas_height) {
    var utils = flag_gen.overlay_utils;
        width = circle_params.x * canvas_width,
        height = circle_params.y * canvas_height,
        radius = utils.get_circle_radius(circle_params.radius, circle_params.radiusdirection, canvas_width, canvas_height),
        draw_circle = utils.draw_circle;
    
    draw_circle(flag, width, height, radius);
    utils.finish_shape(flag, colors[3].hex);

    if (circle_params.outline ==="true"){
        draw_circle(flag, width, height, radius);
        utils.finish_outline(flag, colors[4].hex, circle_params.outline_width);
    }
};
flag_gen.overlay_utils.get_circle_radius = function(radius_param, direction, canvas_width, canvas_height) {
    var radius=0;
    if (direction==='horizontal') {
        radius = radius_param*canvas_width;
    } else {
        radius = radius_param*canvas_height;
    }
    return radius;
}
flag_gen.overlay_utils.draw_circle = function(flag, width, height, radius) {
    flag.save()
    flag.beginPath(); // Start the path
    flag.arc(width,height, radius, 0, Math.PI*2, false ); // Draw a circle
    flag.closePath(); // Close the path
}





// Rays
flag_gen.draw_overlay.rays = function(flag, rays_params, colors, canvas_width, canvas_height){
    
    var count = rays_params.count,
        angle = 360/count,
        x = canvas_width/2,
        y = canvas_height/2,
        offset = rays_params.offset;
    
    flag.save();
    flag.fillStyle=colors[3].hex;
    flag.translate(x,y);
    while (count-- >0){
        flag.beginPath();
        flag.moveTo(0,-offset*canvas_width/2);
        flag.lineTo(0,-canvas_width*2.5);
        flag.rotate(angle/2 * Math.PI/180);
        flag.lineTo(0,-canvas_width*2.5);
        flag.lineTo(0,-offset*canvas_width/2);

        flag.closePath();
        flag.fill();
        flag.rotate(angle/2 * Math.PI/180);
    }
    flag.translate(-x,-y);
    flag.restore();
}




// Slash and X
flag_gen.draw_overlay.slash = function(flag, slash_params, colors, canvas_width, canvas_height) {
    var linewidth = canvas_width * slash_params.width,
        lineheight = canvas_height * slash_params.width,
        color = colors[3].hex;
    
    if (slash_params.direction === 'left-to-right'){
        flag_gen.overlay_utils.draw_ltr_slash(flag, linewidth, lineheight, color, canvas_width, canvas_height);
    }else{
        flag_gen.overlay_utils.draw_rtl_slash(flag, linewidth, lineheight, color, canvas_width, canvas_height);
    }
};

flag_gen.draw_overlay.x = function(flag, x_params, colors, canvas_width, canvas_height) {
    var linewidth = canvas_width * x_params.width,
        lineheight = canvas_height * x_params.width,
        color = colors[3].hex;
    
    flag_gen.overlay_utils.draw_ltr_slash(flag, linewidth, lineheight, color, canvas_width, canvas_height);
    flag_gen.overlay_utils.draw_rtl_slash(flag, linewidth, lineheight, color, canvas_width, canvas_height);
};
flag_gen.overlay_utils.draw_ltr_slash = function(flag, linewidth, lineheight, color, canvas_width, canvas_height) {
    flag.beginPath();
    flag.moveTo(    0,                        0);
    flag.lineTo(    linewidth,                0);
    flag.lineTo(    canvas_width,             canvas_height-lineheight);
    flag.lineTo(    canvas_width,             canvas_height);
    flag.lineTo(    canvas_width-linewidth,   canvas_height);
    flag.lineTo(    0,                        lineheight);
    flag_gen.overlay_utils.finish_shape(flag, color);
};
flag_gen.overlay_utils.draw_rtl_slash = function(flag, linewidth, lineheight, color, canvas_width, canvas_height) {
    flag.beginPath();
    flag.moveTo(    canvas_width-linewidth,   0);
    flag.lineTo(    canvas_width,             0);
    flag.lineTo(    canvas_width,             lineheight);
    flag.lineTo(    linewidth,                canvas_height);
    flag.lineTo(    0,                        canvas_height);
    flag.lineTo(    0,                        canvas_height-lineheight);
    flag_gen.overlay_utils.finish_shape(flag, color);
};
