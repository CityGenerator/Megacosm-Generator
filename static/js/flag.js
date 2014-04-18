
var flag_gen = flag_gen||{};

function create_flag(params,canvas) {
    
    var flag=canvas.getContext('2d'),
        canvas_width=canvas.width,
        canvas_height=canvas.height;

    params.canvas=canvas;//TODO: remove
    params.flag=flag;//TODO: remove
    flag_gen.nest_params(params);
    console.log(params);

    flag_gen.set_ratio( params.ratio['name'],  params.canvas);
    set_shape( params );

    select_division( params);
    select_overlay( params );
    flag_gen.select_symbol( params.flag, params.symbol, params.colors[5].hex, canvas_width, canvas_height );
    //select_border( params );#TODO not implemented, needs to trace shape.
}

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
    
    params.shape=params.shape||{};
}

flag_gen.set_ratio = function(ratio_name, canvas){
    canvas.width=canvas.height*ratio_name;
}



