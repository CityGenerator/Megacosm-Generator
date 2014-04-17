function select_symbol(flag, symbol, color, canvas_width, canvas_height){
    
    if (symbol.name == 'circle'){
        draw_circle_symbol(flag, symbol.circle, color, canvas_width, canvas_height);

    } else if (symbol.name == 'star'){
        draw_star(flag, symbol.star, color, canvas_width, canvas_height);

    } else if (symbol.name=='letter'){
        draw_letter(flag, symbol.letter, color, canvas_width, canvas_height);
    }
}

function draw_circle_symbol(flag, circle_params, color, canvas_width, canvas_height){

    var radius;
    radius=circle_params.radius*canvas_height
    var width=canvas_width*circle_params.x
    var height=canvas_height*circle_params.y
    flag.save();
    flag.beginPath(); // Start the path
    flag.arc(width,height, radius, 0, Math.PI*2, false ); // Draw a circle
    flag.closePath(); // Close the path
    flag.fillStyle=color;
    flag.fill(); // Fill the path
    flag.restore();

}



function draw_letter(flag, letter_params, color, canvas_width, canvas_height){
    flag.fillStyle=color;
    var fontsize=Math.min( canvas_height*letter_params.size  );
    var font= fontsize + "px "+letter_params.fontfamily;

    flag.textBaseline = 'middle';
    flag.font=font;
    flag.fillText(letter_params.letter, (canvas_width*letter_params.x)-fontsize/2   ,(canvas_height*letter_params.y) );

}


function draw_star(flag, star_params, color, canvas_width, canvas_height) {

    var xaxis=star_params.x;
    var yaxis=star_params.y;

    var radius=Math.min( canvas_width*xaxis, canvas_width*(1-xaxis),canvas_height*yaxis, canvas_height*(1-yaxis) );
    flag.fillStyle=color;
    flag.beginPath();
    flag.translate(canvas_width*xaxis, canvas_height*yaxis);
    flag.moveTo(0,0-radius);
    for (var i = 0; i < star_params.points; i++) {
        flag.rotate(Math.PI / star_params.points);
        flag.lineTo(0, 0 - (radius*star_params.inset));
        flag.rotate(Math.PI / star_params.points);
        flag.lineTo(0, 0 - radius);
    }
    flag.fill();
    flag.translate(-canvas_width*xaxis,- canvas_height*yaxis);

}
