// Button Toggle >>>>
document.getElementById("micButton").addEventListener("click", function () {
  const currentText = document.getElementById("tagLine");
  const logo = document.getElementById("logo");

  setTimeout(() => {
    if (currentText.textContent === "Hello, Try Iris!") {
      currentText.textContent = "Listening...";
      logo.style.display="none";
    } else {
      currentText.textContent = "Hello, Try Iris!";
      logo.style.display="block";
    }
  }, 150);
});