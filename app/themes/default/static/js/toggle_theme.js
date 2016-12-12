console.log('theme change');
var themeToggle = document.getElementById('#toggle-theme');

themeToggle.addEventListener('click', function() {

    var xhr = new XMLHttpRequest(); 

    xhr.open("GET", "/theme/test", true); 
    xhr.onload = function(e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
            } else {
                console.error(xhr.statusText);
            }
        }
    };
    xhr.onerror = function(e) {
        console.log(xhr.statusRequest);
    };

    xhr.send(null);

});
