
flag_gen = flag_gen||{};
flag_gen.draw_division = flag_gen.draw_division||{};


flag_gen.select_division = function(flag, division_params, colors, canvas_width, canvas_height){
    
    var type = division_params.name;
    console.log('division: '+type);
    
    if (type==='diagonal' || type==='stripes') {
        flag_gen.draw_division[type](flag, division_params[type], colors, canvas_width, canvas_height);
    }else if (flag_gen.draw_division[type]) {
        flag_gen.draw_division[type](flag, colors, canvas_width, canvas_height);
    }else {
        flag_gen.draw_division['solid'](flag, colors, canvas_width, canvas_height);
        console.log("ERROR: unknown division: "+type+" (flagdivision.js function flag_gen.select_division)");
    }

    /*switch(params.division.name){
        case 'quads':
            draw_quads( params );// colors, canvas
            break;
        case 'diagquads':
            draw_quaddiagonals( params );// colors, canvas
            break;
        case 'diagonal':
            draw_diagonals( params );// diagonal, colors, canvas
            break;
        case 'stripes':
            draw_division_stripes( params );// stripes, colors, canvas
            break;
        case 'none':
            draw_solid( params );// colors, canvas
            break;
        default:
            console.log("ERROR: unknown division:"+params.division.name)
            draw_solid( params );
    }*/
};


flag_gen.draw_division.solid = function(flag, colors, canvas_width, canvas_height) {
    flag.fillStyle = colors[0].hex;
    flag.fillRect(0,0, canvas_width, canvas_height);
};


flag_gen.draw_division.diagquads = function(flag, colors, canvas_width, canvas_height) {
    var directions = ['north', 'south', 'east', 'west'],
        color_nums = [0,0,1,1],
        i=0,
        num_directions = directions.length,
        utils = flag_gen.utils,
        points=[];
    
    for (i=0; i<num_directions; i++) {
        points = utils.get_quaddiag_points(directions[i], canvas_width, canvas_height);
        utils.draw_quaddiag(flag, points, colors[color_nums[i]].hex);
    }
    
};

flag_gen.draw_division.quads = function(flag, colors, canvas_width, canvas_height) {
    var directions = ['nw', 'ne', 'se', 'sw'],
        color_nums = [0,1,0,1],
        i=0,
        num_directions = directions.length,
        points=[];
    
    for (i=0; i<num_directions; i++) {
        points = flag_gen.utils.get_quad_points(directions[i], canvas_width, canvas_height);
        flag.fillStyle = colors[color_nums[i]].hex;
        flag.fillRect(points[0][0], points[0][1], points[1][0], points[1][1]);
    }
}



flag_gen.draw_division.stripes = function(flag, stripe_params, colors, canvas_width, canvas_height) {
    var thickness = 0,
        i=0,
        count = stripe_params.count,
        color_count = stripe_params.colorcount,
        dimension=0,
        draw_stripe,
        color = '';
    
    if (stripe_params.side==='horizontal') {
        thickness = Math.floor(canvas_height/count);
        dimension = canvas_width;
        draw_stripe = flag_gen.utils.draw_stripe_horizontal;
    } else {
        thickness = Math.floor(canvas_width/count);
        dimension = canvas_height;
        draw_stripe = flag_gen.utils.draw_stripe_vertical;
    }
    
    for (i=0; i<count; i++) {
        color = colors[i%color_count].hex;
        draw_stripe(flag, thickness, i, color, dimension);
    }
};


flag_gen.draw_division.diagonal = function(flag, diagonal_params, colors, canvas_width, canvas_height) {
    var start=[],
        mid_north=[],
        mid_south=[],
        end=[],
        draw_diagonal = flag_gen.utils.draw_diagonal;
    
    if (diagonal_params.direction==='left-to-right') {
        start=[0,0];
        mid_north=[canvas_width,0];
        mid_south=[0,canvas_height];
        end=[canvas_width,canvas_height];
    } else {
        start=[canvas_width, 0];
        mid_north=[0,0];
        mid_south=[canvas_width, canvas_height];
        end=[0, canvas_height];
    }
    
    draw_diagonal(flag, start, mid_north, end, colors[0].hex);
    draw_diagonal(flag, start, mid_south, end, colors[1].hex);
};
