function draw_circle_symbol(params){

    var radius;
    radius=params.symbol_circle_radius*params.canvas.height
    var width=params.canvas.width*params.symbol_circle_x
    var height=params.canvas.height*params.symbol_circle_y
    params.flag.save()
    params.flag.beginPath(); // Start the path
    params.flag.arc(width,height, radius, 0, Math.PI*2, false ); // Draw a circle
    params.flag.closePath(); // Close the path
    params.flag.fillStyle=params.colors[5].hex;
    params.flag.fill(); // Fill the path
    params.flag.restore();

}



function draw_letter(params){
    params.flag.fillStyle=params.colors[5].hex;
    var fontsize=Math.min( params.canvas.height*params.symbol_letter_size  );
    var font= fontsize + "px "+params.symbol_letter_fontfamily;

    params.flag.textBaseline = 'middle';
    params.flag.font=font;
    params.flag.fillText(params.letter, (params.canvas.width*params.symbol_letter_x)-fontsize/2   ,(params.canvas.height*params.symbol_letter_y) );

}


function draw_star(params) {

    var xaxis=params.symbol_star_x;
    var yaxis=params.symbol_star_y;

    var radius=Math.min( params.canvas.width*xaxis, params.canvas.width*(1-xaxis),params.canvas.height*yaxis, params.canvas.height*(1-yaxis) );
    params.flag.fillStyle=params.colors[5].hex;
    params.flag.beginPath();
    params.flag.translate(params.canvas.width*xaxis, params.canvas.height*yaxis);
    params.flag.moveTo(0,0-radius);
    for (var i = 0; i < params.symbol_star_points; i++) {
        params.flag.rotate(Math.PI / params.symbol_star_points);
        params.flag.lineTo(0, 0 - (radius*params.symbol_star_inset));
        params.flag.rotate(Math.PI / params.symbol_star_points);
        params.flag.lineTo(0, 0 - radius);
    }
    params.flag.fill();
    params.flag.translate(-params.canvas.width*xaxis,- params.canvas.height*yaxis);

}
