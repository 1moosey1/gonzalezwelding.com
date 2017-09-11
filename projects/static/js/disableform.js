var formElement = document.getElementById("projectform");
formElement.addEventListener("submit", handleFormSubmit);

function handleFormSubmit() {

    var submitElement = document.getElementById("submit"),
        cancelElement = document.getElementById("cancel");

    submitElement.disabled = true;
    cancelElement.style.display = "none";

    submitElement.value = "Processing...";
}
