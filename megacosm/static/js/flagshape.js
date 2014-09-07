
var flag_gen = flag_gen||{};


flag_gen.set_shape = function(flag, shape_params, width, height){
    var draw_shape = flag_gen.draw_shape;
    
    draw_shape.shape_start(flag);
    draw_shape[shape_params.name](flag, width, height, shape_params);// pick the right shape from the draw_shape object
    draw_shape.shape_end(flag);
};

// This object has different functions for drawing different shapes. The object keeps them organized.
flag_gen.draw_shape = {
    shape_start: function(flag) {
        flag.save();
        flag.fillStyle = "rgba(0,0,0,0.0)";
        flag.lineWidth = 1;
    },
    shape_end: function(flag) {
        flag.fill();
        flag.save();
        flag.clip();
    },
    para: function(flag, width, height) {
        flag.moveTo(    0,        0);
        flag.lineTo(    width,    height/6);
        flag.lineTo(    width,    height-height/6);
        flag.lineTo(    0,        height);
    },
    pennant: function(flag, width, height) {
        flag.moveTo(    0,        0);
        flag.lineTo(    width,    height/5*2);
        flag.lineTo(    width,    height/5*3);
        flag.lineTo(    0,        height);
    },
    tri: function(flag, width, height) {
        flag.moveTo(    0,        0);
        flag.lineTo(    width,    height/2);
        flag.lineTo(    0,        height);
    },
    swallow: function(flag, width, height) {
        flag.moveTo(    0,                0);
        flag.lineTo(    width,            height/3*1);
        flag.lineTo(    width-width/5,    height/2);
        flag.lineTo(    width,            height/3*2);
        flag.lineTo(    0,                height);
    },
    square: function(flag, width, height) {
        flag.rect(0,0,width,height);
    },
    tongued: function(flag, width, height, shape_params) {
        var tongue = shape_params.tongue,
            tongue_count = tongue.count,
            tongue_depth = width*tongue.depth,
            tongue_height = height/(tongue_count*2-1),
            tongue_x = width,
            tongue_y = 0,
            draw_tongue_slot = flag_gen.draw_tongue_slot[tongue.type],// get the correct function for drawing this type of tongue slot
            i=0;
        
        flag.moveTo(    0,                0);
        flag.lineTo(    width,            0);
        for (i=0; i<tongue_count; i++) {
            tongue_y = tongue_height*(i*2-1);
            draw_tongue_slot(flag, tongue_x, tongue_y, tongue_depth, tongue_height);
        }
        flag.lineTo(    width,            height);
        flag.lineTo(    0,                height);
    }
};

// object holds a bunch of similar functions for drawing tongue slots
flag_gen.draw_tongue_slot = {
    square: function(flag, x, y, depth, height) {
        flag.lineTo(x,y);
        flag.lineTo(x-depth,y);
        flag.lineTo(x-depth,y+height);
        flag.lineTo(x,y+height);
    },
    triangle: function(flag, x, y, depth, height) {
        flag.lineTo(x,y);
        flag.lineTo(x-depth,y+height/2);
        flag.lineTo(x,y+height);
    },
    scallop: function(flag, x, y, depth, height) {
        flag.lineTo(x,y);
        flag.arc(x, y+height/2 ,height/2 ,1.5 * Math.PI, 0.5*Math.PI,true);
        flag.lineTo(x,y+height);
    },
    sine: function(flag, x, y, depth, height) {
        flag.lineTo(x,y);
        flag.arc(x-height/2, y-height/2,         height/2,     0*Math.PI, 0.5*Math.PI,false);
        flag.arc(x-height/2, y+height/2,         height/2,   1.5*Math.PI, 0.5*Math.PI,true);
        flag.arc(x-height/2, y+height*1.5,       height/2,   1.5*Math.PI, 0*Math.PI,false);
        flag.lineTo(x,y+height);
    }
}
