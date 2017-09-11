// Button must have id 'delete'
var deleteButton = document.getElementById("delete");
deleteButton.addEventListener("click", function() {

    sendDelete();
});

// Handles the xhr request
// django csrf token must be present in html
function sendDelete() {

    // Grab token value
    var token = document.getElementsByName("csrfmiddlewaretoken");
    token = token[0].value;

    // Create request and response handling
    var deleteRequest = new XMLHttpRequest();
    deleteRequest.onreadystatechange = function() {

        // Redirect on location header
        if (deleteRequest.readyState == XMLHttpRequest.DONE) {

            var redirectUrl = deleteRequest.getResponseHeader("Location");
            if(redirectUrl != null) {

                window.location = redirectUrl;
            }
        }
    }

    // Set and send request - assumes delete request going to current URI
    deleteRequest.open("DELETE", "");
    deleteRequest.setRequestHeader("X-CSRFToken", token);
    deleteRequest.send();
}