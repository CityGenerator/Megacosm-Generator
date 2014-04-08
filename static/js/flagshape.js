

function set_shape(params){
    var width=params.canvas.width;
    var height=params.canvas.height;
    params.flag.save();
    params.flag.fillStyle = "rgba(0,0,0,0.0)"
    params.flag.lineWidth = 1
    console.log("shape: "+params.shape['name'])

    switch(params.shape['name']){
        case 'para':
            params.flag.moveTo(    0,        0);
            params.flag.lineTo(    width,    height/6);
            params.flag.lineTo(    width,    height-height/6);
            params.flag.lineTo(    0,        height);
            break;
        case 'pennant':
            params.flag.moveTo(    0,        0);
            params.flag.lineTo(    width,    height/5*2);
            params.flag.lineTo(    width,    height/5*3);
            params.flag.lineTo(    0,        height);
            break;
        case 'tri':
            params.flag.moveTo(    0,        0);
            params.flag.lineTo(    width,    height/2);
            params.flag.lineTo(    0,        height);
            break;
        case 'swallow':
            params.flag.moveTo(    0,                0);
            params.flag.lineTo(    width,            height/3*1);
            params.flag.lineTo(    width-width/5,    height/2);
            params.flag.lineTo(    width,            height/3*2);
            params.flag.lineTo(    0,                height);
            //FIXME swallow depth is not calculated
            //FIXME swallow depth cannot be passed via cli
            break;
        case 'tongued':
            params.flag.moveTo(    0,                0);
            params.flag.lineTo(    width,            0);
            var tonguecount=params.tongued_count;
            var depth=params.tongued_depth;
            for (var i = 0 ; i < tonguecount ; i++){
                params = draw_tongue_slot(params,tonguecount,i,depth,params.tongued_shape);
            }

            params.flag.lineTo(    width,            height);
            params.flag.lineTo(    0,                height);
            break;
        default:
            params.flag.rect(0,0,width,height);
    }
    params.flag.fill();
    params.flag.save();
    params.flag.clip();
    return params.flag;
}


function draw_tongue_slot(params,count,id,depth,type){

    var x = params.canvas.width;
    var height=params.canvas.height/(count*2-1);
    var y = height*(id*2-1);
    depth=params.canvas.width*depth;
    params.flag.lineTo(x,y);
    console.log("Tongueshape: "+type)
    if (type == "square"){
        params.flag.lineTo(x-depth,y);
        params.flag.lineTo(x-depth,y+height);
    }else if (type=="triangle"){
        params.flag.lineTo(x-depth,y+height/2);
    }else if (type=="scallop"){
        params.flag.arc(x, y+height/2 ,height/2 ,1.5 * Math.PI, 0.5*Math.PI,true);
    }else if (type=="sine"){
        params.flag.arc(x-height/2, y-height/2,         height/2,     0*Math.PI, 0.5*Math.PI,false);
        params.flag.arc(x-height/2, y+height/2,         height/2,   1.5*Math.PI, 0.5*Math.PI,true);
        params.flag.arc(x-height/2, y+height*1.5,       height/2,   1.5*Math.PI, 0*Math.PI,false);
    }
    params.flag.lineTo(x,y+height);
    return params;
}

