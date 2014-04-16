

function create_flag(params,canvas) {

    var flag=canvas.getContext('2d');

    params.canvas=canvas;
    params.flag=flag;

    set_ratio( params );
    set_shape( params );

    select_division( params );
    select_overlay( params );
    select_symbol( params );
    //select_border( params );#TODO not implemented, needs to trace shape.
}

function set_ratio(params){
    console.log("ratio: "+params.ratio['name'])
    params.canvas.width=params.canvas.height*params.ratio['name'];
}

function select_symbol(params){

    if (params.symbol.name == 'circle'){
        draw_circle_symbol( params );

    } else if (params.symbol.name == 'star'){
        draw_star(params);

    } else if (params.symbol.name=='letter'){
        draw_letter(params);
    }
}



