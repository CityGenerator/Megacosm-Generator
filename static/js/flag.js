

function create_flag(params,canvas) {
    
    var flag=canvas.getContext('2d');

    params.canvas=canvas;
    params.flag=flag;

    set_ratio( params );
    set_shape( params );
 
    select_division( params );
    select_overlay( params );
    //select_symbol( params );
    //select_border( params );#TODO not implemented
}

function set_ratio(params){
    console.log("ratio: "+params.ratio['name'])
    params.canvas.width=params.canvas.height*params.ratio['name'];
}


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



//
//
//
//
//function select_symbol(params){
//
//    //console.log(params.symbol.name);
//    if (params.symbol.name == 'circle'){
//        draw_circle_symbol( params );
//
//    } else if (params.symbol.name == 'star'){
//        draw_star(params);
//
//    } else if (params.symbol.name=='letter'){
//        draw_letter(params);
//    }
//    return params.flag;
//}
//
//function draw_circle_symbol(params){
//
//    var radius;
//    radius=params.symbol.radius*params.canvas.height
//    var width=params.canvas.width*params.symbol.xlocation
//    var height=params.canvas.height*params.symbol.ylocation
//    params.flag.save()
//    params.flag.beginPath(); // Start the path
//    params.flag.arc(width,height, radius, 0, Math.PI*2, false ); // Draw a circle
//    params.flag.closePath(); // Close the path
//    params.flag.fillStyle=params.colors[5].hex;
//    params.flag.fill(); // Fill the path
//    params.flag.restore();
//
//    return params.flag;
//
//}
//
//function draw_letter(params){
//    params.flag.fillStyle=params.colors[5].hex;
//    var fontsize=Math.min( params.canvas.height*params.symbol.size  );
//    var font= fontsize + "px "+params.symbol.fontfamily;
//
//    params.flag.textBaseline = 'middle';
//    params.flag.font=font;
//    //console.log(font);
//    params.flag.fillText(params.symbol.letter, (params.canvas.width*params.symbol.xlocation)-fontsize/2   ,(params.canvas.height*params.symbol.ylocation) );
//
//    return params.flag;
//}
//
//
//

//
//    
//    function draw_x(flag, width, height, thickness, color){
//        var linewidths=Array( 1/6, 1/8, 1/9, 1/10, 1/12, 1/15, 1/20);
//        thickness = thickness|| linewidths[ d( linewidths.length ) ] ;
//        flag=draw_slash(flag,width,height,thickness,'left',color);
//        flag=draw_slash(flag,width,height,thickness,'right',color);
//        return flag;
//    }
//
//
//
//    function draw_border(flag, width, height, thickness,colorlist){
//        thickness=thickness|| d(10)+2 ;
//        var color=colorlist[2] ||random_color();
//        flag.beginPath();
//        flag.lineWidth=thickness;
//        flag.moveTo(0+thickness/2,0+thickness/2);
//        flag.lineTo(width-thickness/2,0+thickness/2);
//        flag.lineTo(width-thickness/2,height-thickness/2);
//        flag.lineTo(0+thickness/2,height-thickness/2);
//        flag.lineTo(0+thickness/2,0);
//        flag.strokeStyle=color;
//        flag.stroke();
//        return flag;
//    
//    }
//    
//    
//
//
//function draw_star(params) {
//
//
//    var xaxis=params.symbol.xlocation;
//    var yaxis=params.symbol.ylocation;
//    
//    var radius=Math.min( params.canvas.width*xaxis, params.canvas.width*(1-xaxis),params.canvas.height*yaxis, params.canvas.height*(1-yaxis) );
//    params.flag.fillStyle=params.colors[5].hex;
//    params.flag.beginPath();
//    params.flag.translate(params.canvas.width*xaxis, params.canvas.height*yaxis);
////console.log("x "+ (params.canvas.width)+" y "+(params.canvas.height));
////console.log("x "+ (xaxis)+" y "+(yaxis));
////console.log("x "+ (params.canvas.width*xaxis)+" y "+(params.canvas.height*yaxis));
//    params.flag.moveTo(0,0-radius);
//    for (var i = 0; i < params.symbol.points; i++) {
//        params.flag.rotate(Math.PI / params.symbol.points);
//        params.flag.lineTo(0, 0 - (radius*params.symbol.inset));
//        params.flag.rotate(Math.PI / params.symbol.points);
//        params.flag.lineTo(0, 0 - radius);
//    }
//    params.flag.fill();
//    params.flag.translate(-params.canvas.width*xaxis,- params.canvas.height*yaxis);
//    return params.flag;
//}
//
//

    

 

////    function getQueryString() {
////        var result = {}, queryString = location.search.substring(1),
////            re = /([^&=]+)=([^&]*)/g, m;
////        while (m = re.exec(queryString)) {
////            result[decodeURIComponent(m[1])] = decodeURIComponent(m[2]);
////        }
////        return result;
////    }
//
////    /* ************************************************************* */
////    /*
////    /*  This is a quick and dirty function to select five
////    /*  non-repeating colors for the flag.
////    /*  colors[0] is the base
////    /*  colors[1] is the division secondary
////    /*  colors[2] is the division tertiary (optional)
////    /*  colors[3] is the overlay
////    /*  colors[4] is the symbol
////    /*
////    /* ************************************************************* */
//
//
//
//
