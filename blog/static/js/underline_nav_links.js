/*
 * set of links.
 * each window location maps to a link element, applies an id 
 *
 */

console.log('pathname!: ', window.location.pathname);

var routes = {
  '' :                    'blog',
  'index.html'      :     'blog',
  'index'           :     'blog',
  'projects.html'   :     'projects',
  'projects'        :     'projects',
  'guides.html'     :     'guides',
  'guides'          :     'guides',
  'fun.html'        :     'fun',
  'fun'             :     'fun',
  'about.html'      :     'about-me',
  'about'           :     'about-me',
  'posts'           :     'blog',
};

// get current location path
var currentWindowLocation = window.location.pathname.slice(1).split('/')[0];

// look it up and get the corresponding id
var targetElementId = routes[currentWindowLocation];

if (targetElementId) {
  var targetElement = document.getElementById(targetElementId);
  targetElement.className += ' current-page-highlight';
}

else if (currentWindowLocation in routes) {
  console.log('you have an incorrectly configured script');
}
// target the element with that id
