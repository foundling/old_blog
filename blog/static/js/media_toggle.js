var mediaUpClass = 'media-up';
var mediaDownClass = 'media-down';
var up = true;
var cn;

var socialMedia = document.getElementById('social-media');
socialMedia.onclick = function(e) {
    up = !up;
    if (!up) e.target.className = e.target.className.replace(mediaUpClass,mediaDownClass);
    if (up) e.target.className = e.target.className.replace(mediaDownClass,mediaUpClass);
    console.log(e.target.className);
    console.log(up);
};
