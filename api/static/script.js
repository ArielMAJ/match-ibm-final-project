function submitForm(e) {
  e.preventDefault();

  var myform = document.getElementById("mainAppForm");

  var formData = new FormData(myform);

  fetch("https://localhost:3000/goal", {
    method: "POST",
    headers: {
      "Content-Type": "application/json", // Set Content-Type header to application/json
    },
    body: { formData },
  })
    .then((response) => {
      if (!response.ok && response.status != 400) {
        throw new Error("network returns error");
      }
      return response.json();
    })
    .then((resp) => {
      // write a post request with json value message to '/'
    })
    .catch((error) => {
      // Handle error
      console.log("error ", error);
    });
}

function writeGoal() {
  console.log("test");
  let message = "Test message";
  fetch("https://localhost:3000/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json", // Set Content-Type header to application/json
    },
    body: { message: message },
    redirect: "follow",
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("network returns error");
      }
      return response.json();
    })
    .then((resp) => {
      // write a post request with json value message to '/'
    })
    .catch((error) => {
      // Handle error
      console.log("error ", error);
    });
}

// var myform = document.getElementById("mainAppFormSubmitButton");

// myform.addEventListener("click", writeGoal);

var element = document.getElementById("mainAppFormSubmitButton");

element.addEventListener("mouseover", function (e) {
  console.log("test");
});
