document.addEventListener("DOMContentLoaded", () => {
  const video = document.getElementById("video");
  const captureButton = document.getElementById("captureButton");
  const previewImage = document.getElementById("previewImage");
  const newCaptureButton = document.getElementById("newCaptureButton");
  const canvas = document.createElement("canvas");
  const context = canvas.getContext("2d");
  const submitCapture = document.getElementById("submit-capture");
  const responseText = document.getElementById("response-text");

  function startVideo() {
    navigator.getUserMedia(
      { video: {} },
      (stream) => (video.srcObject = stream),
      (err) => console.error(err)
    );
  }

  startVideo();

  captureButton.addEventListener("click", () => {
    video.style.display = "none";
    previewImage.style.display = "block";
    captureButton.style.display = "none";
    newCaptureButton.style.display = "block";
    submitCapture.style.display = "block";
    responseText.innerText = "Image captured!";

    captureAndPreview();
  });

  newCaptureButton.addEventListener("click", () => {
    video.style.display = "block";
    previewImage.style.display = "none";
    captureButton.style.display = "block";
    newCaptureButton.style.display = "none";
    submitCapture.style.display = "none";
    responseText.innerText = "";

    startVideo();
  });

  submitCapture.addEventListener("click", () => {
    send();
  });

  let imageData;
  function captureAndPreview() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    // Flip the image horizontally
    // context.translate(canvas.width, 0);
    // context.scale(-1, 1);

    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Reset the transformation matrix
    // context.setTransform(1, 0, 0, 1, 0, 0);
    imageData = canvas.toDataURL("image/jpeg");
    // Display the captured image
    previewImage.src = imageData;
  }

  function send() {
    sendDataToDjango(imageData);
    window.location.href = "/textOcr/";
  }

  function sendDataToDjango(imageDataURL) {
    // Use AJAX or fetch to send the data to Django
    fetch("/capture/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ image_data: imageDataURL }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error("Error:", error));
  }
});
