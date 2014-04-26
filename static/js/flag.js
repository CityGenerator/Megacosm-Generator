
var flag_gen = flag_gen||{};

function create_flag(params,canvas) {
    
    var flag=canvas.getContext('2d'),
        canvas_width=0,
        canvas_height=0;

    params.canvas=canvas;//TODO: remove
    params.flag=flag;//TODO: remove
    flag_gen.nest_params(params);
    console.log(params);

    flag_gen.set_ratio( params.ratio['name'],  canvas);
    canvas_width=canvas.width,
    canvas_height=canvas.height;
    
    flag_gen.set_shape( params.flag, params.shape, canvas_width, canvas_height );

    select_division( params);
    flag_gen.select_overlay( params.flag, params.overlay, params.colors, canvas_width, canvas_height );
    flag_gen.select_symbol( params.flag, params.symbol, params.colors[5].hex, canvas_width, canvas_height );
    //select_border( params );#TODO not implemented, needs to trace shape.
};

flag_gen.nest_params = function(params){
    
    params.symbol=params.symbol||{};
    params.symbol.circle={
        radius: params.symbol_circle_radius || null,
        x:      params.symbol_circle_x || null,
        y:      params.symbol_circle_y || null
    };
    params.symbol.star={
        x:      params.symbol_star_x||null,
        y:      params.symbol_star_y||null,
        points: params.symbol_star_points || null,
        inset:  params.symbol_star_inset || null
    };
    params.symbol.letter={
        x:          params.symbol_letter_x||null,
        y:          params.symbol_letter_y||null,
        size:       params.symbol_letter_size||null,
        fontfamily: params.symbol_letter_fontfamily||null,
        letter:     params.letter||null,
    };
    
    params.division=params.division||{};
    
    params.overlay=params.overlay||{};
    params.overlay.name='quaddiag';//TODO: remove
    params.overlay.circle={
        outline:            params.overlay_circle_outline,
        outlinewidth:       params.overlay_circle_outlinewidth,
        radius:             params.overlay_circle_radius,
        radiusdirection:    params.overlay_circle_radiusdirection,
        x:                  params.overlay_circle_x,
        y:                  params.overlay_circle_y
    };
    params.overlay.cross={
        horlength:          params.overlay_cross_horlength,
        horpos:             params.overlay_cross_horpos,
        horwidth:           params.overlay_cross_horwidth,
        vertlength:         params.overlay_cross_vertlength,
        vertwidth:          params.overlay_cross_vertwidth
    };
    params.overlay.diamond={
        outline:            params.overlay_diamond_outline
    };
    params.overlay.quad={
        side:               params.overlay_quad_side
    };
    params.overlay.quaddiag={
        side:               params.overlay_quaddiag_side
    };
    params.overlay.rays={
        count:              params.overlay_rays_count,
        offset:             params.overlay_rays_offset,
        x:                  params.overlay_rays_x,
        y:                  params.overlay_rays_y
    };
    params.overlay.slash={
        direction:          params.overlay_slash_direction,
        width:              params.overlay_slash_width
        
    };
    params.overlay.stripe={
        count:              params.overlay_stripe_count,
        countselected:      params.overlay_stripe_countselected,
        side:               params.overlay_stripe_side
    };
    params.overlay.x={
        outline:            params.overlay_x_outline,
        width:              params.overlay_x_width
    };
    
    params.shape=params.shape||{};
    params.shape.tongue={
        depth:  params.shape_tongued_depth,
        width:  params.shape_tongued_width,
        shape:  params.shape_tongued_shape,
        count:  params.shape_tongued_count,
        type:   params.shape_tongued_shape
    };
};

flag_gen.set_ratio = function(ratio_name, canvas){
    canvas.width=canvas.height*ratio_name;
};



