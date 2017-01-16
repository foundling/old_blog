const GRAVITY = 0.5;

const Player = function(imgs, ctx, coordinates, mass) {

    if (!imgs || !imgs.length) throw new Error('Player object needs one or more images with source properties.');
    if (!ctx || !ctx.canvas) throw new Error('Player object must be instantiated with a canvas object reference');
    if (!(coordinates.x && coordinates.y)) throw new Error('Player object must be instantiated with x and y coordinates.');

    let images = {
        left: imgs[0],
        right: imgs[1]
    };
    let imageDirection = 'right';
    let img = images[imageDirection];
    let velocity = {
        x: 0, 
        y: -8,
    };
    const moves = {
        jump: function(e) {
            if (e.key === 'ArrowUp') {
                animate();
                console.log(velocity)
                console.log(coordinates)
            }
        },
        moveLeft: function(e) {
            if (e.key === 'ArrowLeft') {
                updateDirection('left');
                console.log(e.key);
            }
        },
        moveRight: function(e) {
            if (e.key === 'ArrowRight') {
                updateDirection('right');
                console.log(e.key);
            }
        }
    }

    Object.keys(moves).forEach(key => document.addEventListener('keydown', moves[ move ]));

    function redraw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, coordinates.x, coordinates.y); 
    }
    function updateState() {
        velocity.y += GRAVITY;
        coordinates.y += velocity.y;
        coordinates.x += velocity.x;  
    }
    function animate() {
        let intervalHandle = setInterval(function() {
            console.log('loop');

            updateState()
            redraw();

            if (coordinates.y + img.height >= canvas.height) {
                clearInterval(intervalHandle);
            } 
        }, 1000/60); 

    }
    function updateDirection(key) {
        if (imageDirection === 'right' && key === 'left') {

            imageDirection = 'left';
            img = images[imageDirection];
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, coordinates.x, coordinates.y);

        } else if (imageDirection === 'left' && key === 'right') {

            imageDirection = 'right';
            img = images[imageDirection];
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, coordinates.x, coordinates.y);

        }

    }
    function init() {
        ctx.drawImage(img, coordinates.x, coordinates.y); 
    }

    return {
        init,
        update
    };

};

const log = console.log;

function run() {

    log('Initializing Calvin ...');

    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const imgs = [ new Image(), new Image() ];
    let imagesLoaded = 0;

    canvas.width = 600;
    canvas.height = 600;
    imgs[0].src = 'calvin-left.png';
    imgs[1].src = 'calvin-right.png';

    imgs.forEach(function(img) {

        img.addEventListener('load', function() {

            if ( ++imagesLoaded < 2 ) return;

            const calvin = new Player(imgs, ctx, {x: 100, y: 150}, 100);
            calvin.init();

        });

    });
}

run();
