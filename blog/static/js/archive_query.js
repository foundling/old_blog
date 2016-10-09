var query = (window.location.href.split('?').length > 1) ? window.location.href.split('?')[1].split('=') : null;
var archiveSearch = document.getElementById('archive-search');

if (query) {
  archiveSearch.value = query[1];
}
