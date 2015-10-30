// distance from top of document
// window distance from top
// state change occurs when window offset from top of doc is greater than the element's distance from top, which is fixed 
var socialMedia = document.getElementById('social-media');
var headerHeight = 90;
var pastHeader = false;
var arrowEl = document.getElementById('to-top');

arrowEl.onclick = function() { window.scrollTo(0,0)}




var checkWindowOffsetFromTop = function(event) {
  var windowOffsetY = window.pageYOffset;
  if (windowOffsetY > headerHeight) {
    pastHeader = true;
    console.log('past header');  
    arrowEl.style.display ='block';
  }
  else {
    console.log('not past header');  
    pastHeader = false;
    arrowEl.style.display ='none';
  }
};

window.onscroll = checkWindowOffsetFromTop;
