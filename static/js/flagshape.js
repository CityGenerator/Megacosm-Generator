
var flag_gen = flag_gen||{};


flag_gen.set_shape = function(flag, shape_params, canvas_width, canvas_height){
    var tounge_count=0,
        tounge_depth=0,
        tounge_type='',
        shape_lines_count=0,
        i=0;
    
    
    var shape_lines = flag_gen.get_shape_lines(shape_params, canvas_width, canvas_height);
    
    
    flag.save();
    flag.fillStyle = "rgba(0,0,0,0.0)"
    flag.lineWidth = 1
    
    if (shape_lines === 'tounged') {
        tounge_count = shape_params.tounge.count;
        tounge_type = shape_params.tounge.type;
        tounge_depth = shape_params.tounge.depth;
        
        flag.lineTo(canvas_width, 0);
        
        i=0;
        for (i=0; i<tounge_count; i++) {
            flag_gen.draw_tounge_slot(flag, flag_gen.get_tounge_slot(i, tounge_count, tounge_depth, tounge_type, canvas_width, canvas_height));
        }
        
        flag.lineTo(0, canvas_height);
    }
    else {
        if (shape_lines.length === 0) {
            flag.rect(0,0,canvas_width,canvas_height);// square
        }
        else {
            flag.moveTo(0, 0);
            shape_lines_count = shape_lines.length,
            i = 0;
            for (i; i<shape_lines_count; i++) {
                flag.lineTo(shape_lines[i][0], shape_lines[i][1]);
            }
        }
    }
    
    flag.fill();
    flag.save();
    flag.clip();
    return flag;
};


flag_gen.get_shape_lines = function(shape_params, width, height) {
    
    var shape_lines = [];
    
    switch(shape_params['name']){
        case 'para':
            shape_lines = [
                [width,         height/6],
                [width,         height-height/6],
                [0,             height]
            ];
            break;
        case 'pennant':
            shape_lines = [
                [width,         height/5*2],
                [width,         height/5*3],
                [0,             height]
            ];
            break;
        case 'tri':
            shape_lines = [
                [width,         height/2],
                [0,             height]
            ];
            break;
        case 'swallow':
            shape_lines = [
                [width,         height/3*1],
                [width-width/5, height/2],
                [width,         height/3*2],
                [0,             height]
            ];
            //FIXME swallow depth is not calculated
            //FIXME swallow depth cannot be passed via cli
            break;
        case 'tounged':
            shape_lines='tounged';
            break;
    }
    console.log(shape_lines);
    return shape_lines;
};


/*
 params.shape.tounge={
        depth:  params.tounged_depth,
        width:  params.tounged_width,
        shape:  params.tounged_shape,
        count:  params.tounged_count
    };
*/
flag_gen.get_tounge_slot = function(id, count, depth_ratio, type, canvas_width, canvas_height) {
    var height  = canvas_height/(count*2-1),
        x       = canvas_width,
        y       = height*(id*2-1),
        depth   = canvas_width*depth_ratio,
        tounge_slot = [];
        
    switch(type){
        case 'square':
            tounge_slot = [
                [x, y],
                [x-depth,   y],
                [x-depth,   y+height]
            ];
            break;
        case 'triangle':
            tounge_slot = [
                [x, y],
                [x-depth,   y+height/2]
            ];
            break;
        case 'scallop':
            tounge_slot = [
                [x, y],
                [x, y+height/2 ,height/2 ,1.5 * Math.PI, 0.5*Math.PI,true]
            ];
            break;
        case 'sine':
            tounge_slot = [
                [x, y],
                [x-height/2, y-height/2, height/2, 0*Math.PI, 0.5*Math.PI,false],
                [x-height/2, y+height/2, height/2, 1.5*Math.PI, 0.5*Math.PI,true],
                [x-height/2, y+height*1.5,       height/2,   1.5*Math.PI, 0*Math.PI,false]
            ];
            break;
    }
    tounge_slot.push([x, y+height]);
    return tounge_slot;
};
flag_gen.draw_tounge_slot = function(flag, tounge_slot) {
    var count = tounge_slot.length,
        i = 0,
        slot = {};
    
    for (i; i<count; i++) {
        slot = tounge_slot[i];
        if (slot.length===2) {
            flag.lineTo(slot[0], slot[1]);
        }
        else {
            flag.arc(slot[0], slot[1], slot[2], slot[3], slot[4], slot[5]);
        }
    }
}


flag_gen.draw_tounge_slot = function(params,count,id,depth,type){

    var x = canvas_width;
    var height=canvas_height/(count*2-1);
    var y = height*(id*2-1);
    depth=canvas_width*depth;
    flag.lineTo(x,y);
    console.log("Tongueshape: "+type)
    if (type == "square"){
        flag.lineTo(x-depth,y);
        flag.lineTo(x-depth,y+height);
    }else if (type=="triangle"){
        flag.lineTo(x-depth,y+height/2);
    }else if (type=="scallop"){
        flag.arc(x, y+height/2 ,height/2 ,1.5 * Math.PI, 0.5*Math.PI,true);
    }else if (type=="sine"){
        flag.arc(x-height/2, y-height/2,         height/2,     0*Math.PI, 0.5*Math.PI,false);
        flag.arc(x-height/2, y+height/2,         height/2,   1.5*Math.PI, 0.5*Math.PI,true);
        flag.arc(x-height/2, y+height*1.5,       height/2,   1.5*Math.PI, 0*Math.PI,false);
    }
    flag.lineTo(x,y+height);
    return params;
};

