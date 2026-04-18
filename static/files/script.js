function handleQuizSubmit() {
    const button = document.getElementById("submitBtn");

    if (button) {
        button.innerText = "Calculating...";
        button.disabled = true;
    }
}

console.log("JS Loaded");
