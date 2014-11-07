
flag_gen = flag_gen||{};

flag_gen.utils = {
    
    get_quaddiag_points: function(direction, canvas_width, canvas_height) {
        
        var points = [],
            i = 0;
        
        switch(direction) {
            case 'north':
                points = [[1,1],[0,1]];
                break;
            case 'east':
                points = [[1,1],[1,0]];
                break;
            case 'south':
                points = [[0,0],[1,0]];
                break;
            case 'west':
                points = [[0,0],[0,1]];
                break;
        }
        points[2] = [.5,.5];
        
        for (i=0; i<3; i++) {
            points[i][0] = points[i][0]*canvas_width;
            points[i][1] = points[i][1]*canvas_height;
        }
        return points;
    },
    draw_quaddiag: function(flag, points, color) {
        flag.save();
        flag.beginPath();
        flag.moveTo(points[0][0], points[0][1]);
        flag.lineTo(points[1][0], points[1][1]);
        flag.lineTo(points[2][0], points[2][1]);
        flag.fillStyle = color;
        flag.fill();
    },
    get_quad_points: function(direction, canvas_width, canvas_height) {
        var ns = direction.charAt(0),
            ew = direction.charAt(1),
            points = [[],[]],
            i = 0;
        
        if (ew === 'w') {
            points[0][0] = 0;
            points[1][0] = .5;
        } else {
            points[0][0] = .5;
            points[1][0] = 1;
        }
        
        if (ns === 'n') {
            points[0][1] = 0;
            points[1][1] = .5;
        } else {
            points[0][1] = .5;
            points[1][1] = 1;
        }
        
        for (i=0; i<2; i++) {
            points[i][0] = points[i][0]*canvas_width;
            points[i][1] = points[i][1]*canvas_height;
        }
        return points;
    },
    draw_stripe_horizontal: function(flag, thickness, id, color, canvas_width) {
        var start = thickness * id;
        flag.fillStyle = color;
        flag.fillRect(0, start, canvas_width, thickness);
    },
    draw_stripe_vertical: function(flag, thickness, id, color, canvas_height) {
        var start = thickness * id;
        flag.fillStyle = color;
        flag.fillRect(start, 0, thickness, canvas_height);
    },
    draw_diagonal: function(flag, start, mid, end, color) {
        flag.save();
        flag.beginPath();
        flag.moveTo(start[0],start[1]);
        flag.lineTo(mid[0],mid[1]);
        flag.lineTo(end[0],end[1]);
        flag.fillStyle=color;
        flag.fill();
        flag.restore();
    }
    
    
};