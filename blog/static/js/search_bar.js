var inputEngaged = false; 
var mediaBar = document.getElementById('social-media');
var searchIcon = mediaBar.querySelector('#search-icon');
var searchIconInput = mediaBar.querySelector('#search-icon-input');

var cachedClassInfo = {
  'searchIcon': searchIcon.className,
  'searchIconInput' : searchIconInput.className
};

var body = document.body;

var toggleSearch = function (e) {
  if (e.target.id === 'search-icon') {
    searchIcon.className = 'invisible';
    searchIconInput.className = 'visible';
    inputEngaged = true;
  }
  else if (inputEngaged && e.target.id != 'search-icon-input') {
    searchIcon.className = cachedClassInfo['searchIcon'];
    searchIconInput.className = cachedClassInfo['searchIconInput'];
  }
 

};

body.addEventListener('click', toggleSearch);

