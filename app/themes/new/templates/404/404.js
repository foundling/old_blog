const log = console.log;
const gravity = 9.8;

function init() {

    log('Initializing Calvin ...');

    const canvas = document.getElementById('canvas');
    canvas.width = 600;
    canvas.height = 600;
    const ctx = canvas.getContext('2d');
    const img = new Image();
    img.src = 'http://pleated-jeans.com/wp-content/uploads/2011/02/calvin-and-hobbes-nes-sprite1.png'; //'calvin.png';
    img.addEventListener('load', function() {

        console.log('image loaded');
        const calvin = new Player(img, { x: 100, y: 150 });
        ctx.drawImage(calvin.img, 10, 0); 
        console.log(img);
        //loop(calvin, canvas, ctx);

    });

}

function loop(player, canvas, ctx) {

    let intervalHandle = setInterval(function() {

        player.update();

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(player.img, player.x, player.y); 

    }, 1000/60);

}


const Player = function(img, coordinates) {

    if (!(coordinates.x && coordinates.y)) {
        throw new Error('Player object must be instantiated with x and y coordinates.');
    }

    const attrs = {
        weight: 100,
        coordinates: coordinates
    };

    const moves = [

        function jump(e) {
            if (e.key === 'ArrowUp') {
                console.log(e.key);
            }
        },
        function moveLeft(e) {
            if (e.key === 'ArrowLeft') {
                console.log(e.key);
            }
        },
        function moveRight(e) {
            if (e.key === 'ArrowRight') {
                console.log(e.key);
            }
        }
    ];

    function update(x,y) {
        // coordinates.x += x;
        // coordinates.y += y;
    };

    moves.forEach(move => document.addEventListener('keydown', move));

    return {
        img,
        coordinates,
        update
    };

    // reverse image on y axis
    // jump up, left or right
    // move left or right 

};

// redraw function to update canvas
// keypress bindings
//
init();
