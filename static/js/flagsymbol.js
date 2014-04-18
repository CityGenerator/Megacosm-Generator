
var flag_gen = flag_gen||{};

flag_gen.select_symbol = function(flag, symbol, color, canvas_width, canvas_height){console.log(symbol.name);
    
    if (symbol.name === 'circle'){
        flag_gen.draw_circle_symbol(flag, flag_gen.get_circle_symbol(symbol.circle, color, canvas_width, canvas_height) );

    } else if (symbol.name === 'star'){
        flag_gen.draw_star_symbol(flag, flag_gen.get_star_symbol(symbol.star, color, canvas_width, canvas_height));

    } else if (symbol.name === 'letter'){
        flag_gen.draw_letter_symbol(flag, flag_gen.get_letter_symbol(symbol.letter, color, canvas_width, canvas_height));
    }
};

flag_gen.get_circle_symbol = function(circle_params, color, canvas_width, canvas_height){
    var circle_symbol = {
        radius: circle_params.radius*canvas_height,
        width:  canvas_width*circle_params.x,
        height: canvas_height*circle_params.y,
        color:  color
    };
    return circle_symbol;
};
flag_gen.draw_circle_symbol = function(flag, circle_symbol){
    flag.save();
    flag.beginPath(); // Start the path
    flag.arc(circle_symbol.width, circle_symbol.height, circle_symbol.radius, 0, Math.PI*2, false ); // Draw a circle
    flag.closePath(); // Close the path
    flag.fillStyle=circle_symbol.color;
    flag.fill(); // Fill the path
    flag.restore();
};


flag_gen.get_letter_symbol = function(letter_params, color, canvas_width, canvas_height){
    var fontsize = Math.min(canvas_height*letter_params.size),
        letter_symbol = {
            fontsize:   fontsize,
            font:       fontsize + "px "+letter_params.fontfamily,
            color:      color,
            letter:     letter_params.letter,
            x:          (canvas_width*letter_params.x)-fontsize/2,
            y:          canvas_height*letter_params.y
        };
    return letter_symbol;
};
flag_gen.draw_letter_symbol = function(flag, letter_symbol){
    flag.fillStyle = letter_symbol.color;
    flag.textBaseline = 'middle';
    flag.font = letter_symbol.font;
    flag.fillText(letter_symbol.letter, letter_symbol.x, letter_symbol.y);

};


flag_gen.get_star_symbol = function(star_params, color, canvas_width, canvas_height) {
    var xaxis = star_params.x,
        yaxis = star_params.y,
        star_symbol = {
            xaxis:          xaxis,
            yaxis:          yaxis,
            radius:         Math.min( canvas_width*xaxis, canvas_width*(1-xaxis),canvas_height*yaxis, canvas_height*(1-yaxis) ),
            color:          color,
            points:         star_params.points,
            inset:          star_params.inset,
            x_translation:  canvas_width*xaxis,
            y_translation:  canvas_height*yaxis
        };
    return star_symbol;
};
flag_gen.draw_star_symbol = function(flag, star_symbol) {
    flag.fillStyle=star_symbol.color;
    flag.beginPath();
    flag.translate(star_symbol.x_translation, star_symbol.y_translation);
    flag.moveTo(0,0-star_symbol.radius);
    for (var i = 0; i < star_symbol.points; i++) {
        flag.rotate(Math.PI / star_symbol.points);
        flag.lineTo(0, 0 - (star_symbol.radius*star_symbol.inset));
        flag.rotate(Math.PI / star_symbol.points);
        flag.lineTo(0, 0 - star_symbol.radius);
    }
    flag.fill();
    flag.translate(-star_symbol.x_translation, -star_symbol.y_translation);
};


