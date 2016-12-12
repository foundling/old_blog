var inputEngaged = false; 
var mediaBar = document.getElementById('social-media');
var searchIcon = mediaBar.querySelector('#search-icon');
var searchIconInput = mediaBar.querySelector('#search-icon-input');

var cachedClassInfo = {
  'searchIcon': searchIcon.className,
  'searchIconInput' : searchIconInput.className
};

var body = document.body;

var toggleOut = function(e) {
    e.preventDefault();
    searchIcon.className = 'invisible';
    searchIconInput.className = 'visible';
    searchIconInput.focus();
    inputEngaged = true;
};

var toggleIn = function(e) {
    searchIcon.className = cachedClassInfo['searchIcon'];
    searchIconInput.className = cachedClassInfo['searchIconInput'];
    searchIconInput.blur();
};

var toggleSearch = function (e) {
  if (e.target.id === 'search-icon') {
    toggleOut(e);
  }
  else if (inputEngaged && e.target.id != 'search-icon-input') {
    toggleIn(e);
  }
 

};

body.addEventListener('click', toggleSearch);
body.addEventListener('keydown',toggleSearch);
