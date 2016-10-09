var socialMedia = document.getElementById('social-media');
var arrowEl = document.getElementById('to-top');
var header = document.querySelector('ul.header');
var headerHeight = header.offsetHeight;
var arrowEngaged = window.pageYOffset > headerHeight;
if (arrowEngaged) {
    arrowEl.className = '';
}
var offsetTop;

arrowEl.onclick = function() { 
  window.scrollTo(0,0);
};

var checkOffsetTop = function(event) {

  offsetTop = window.pageYOffset;

  if (offsetTop >= headerHeight) {
      if (arrowEngaged) {
          return;
      }
      console.log('flipped');
      arrowEngaged = true;
      arrowEl.className = '';
  }
  else {
      if (!arrowEngaged) {
          return;
      }
      console.log('flipped');
      arrowEngaged = false;
      arrowEl.className = 'hidden';
  }
};

window.onscroll = checkOffsetTop;
