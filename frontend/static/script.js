document.getElementById("uploadBtn").addEventListener("click", function() {
    let fileInput = document.getElementById("resumeInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select a PDF file to upload.");
        return;
    }

    let formData = new FormData();
    formData.append("resume", file);

    document.getElementById("loading").style.display = "block"; // Show loading spinner

    fetch("/upload", {  // Change to backend URL
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("loading").style.display = "none"; // Hide spinner
        document.getElementById("result").style.display = "block"; // Show results

        document.getElementById("name").innerText = data.name || "Not Found";
        document.getElementById("skills").innerText = data.skills.join(", ") || "None";
        document.getElementById("experience").innerText = data.experience || "0";
        document.getElementById("projects").innerText = data.projects.join(", ") || "None";
        document.getElementById("score").innerText = data.score || "0";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("loading").style.display = "none";
        alert("Error processing resume.");
    });
});

document.getElementById("resumeInput").addEventListener("change", function () {
    // Clear previous results when a new file is selected
    document.getElementById("result").style.display = "none";
});