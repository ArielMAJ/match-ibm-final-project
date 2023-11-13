function clearForm(event) {
  // Prevent the default form submission
  event.preventDefault();

  var responseMessage = document.getElementById("response-message");
  if (responseMessage) {
    responseMessage.remove();
  }
  var form = document.getElementById("myForm");
  form.reset();
}

function showToast() {
  let toast = document.getElementById("toast");
  toast.style.transform = "translateX(0)";
  setTimeout(() => {
    toast.style.transform = "translateX(500px)";
  }, 4000);
  setTimeout(() => {
    toast.remove();
  }, 5000);
}

function closeToast() {
  let toast = document.getElementById("toast");
  toast.remove();
  if (toast) {
    toast.remove();
  }
}

function btnFunction(btnId, btnTextId, rndWord) {
  let submitBtn = document.querySelector(btnId);
  let submitBtnText = document.querySelector(btnTextId);
  let originalBtnTextValue = submitBtnText.innerHTML;

  submitBtn.disabled = true;
  if (rndWord) {
    submitBtnText.innerHTML = getRandomPositiveMessage();
  }
  submitBtn.classList.add("active");

  setTimeout(() => {
    submitBtnText.innerHTML = originalBtnTextValue;
    submitBtn.classList.remove("active");
    submitBtn.disabled = false;
  }, 3000);
}

function getRandomPositiveMessage() {
  var congratulationsMessages = [
    "Parabéns!",
    "Isso aí!",
    "Fantástico!",
    "Bom trabalho!",
    "Sensacional!",
    "Incrível!",
    "Você é demais!",
    "Ótimo trabalho!",
    "Viva!",
    "Ihuu!",
    "Continue assim!",
    "Bravo!!",
    "Muito bem!",
    "Rico!",
    "Legal!",
    "Indo bem!",
    "💵💵💵",
    "💶💶💶",
    "💷💷💷",
    "💵💶💷",
  ];

  // Randomly select a message
  var randomIndex = Math.floor(Math.random() * congratulationsMessages.length);

  return congratulationsMessages[randomIndex];
}

function delaySubmit(event) {
  // Prevent the default form submission
  event.preventDefault();

  var form = document.getElementById("myForm");

  setTimeout(() => {
    form.submit();
  }, 2000);
}
