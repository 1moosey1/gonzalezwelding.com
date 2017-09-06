// Remove alerts after three seconds
// Alert div must have the id 'alert'
window.setTimeout(function() {

    var alert = document.getElementById("alert");

    if(alert)
        alert.style.display = "none";

}, 3000);