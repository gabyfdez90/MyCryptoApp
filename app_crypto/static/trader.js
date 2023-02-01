function addTableRow() {
  var table = document.getElementById("trading-table");
  var row = table.insertRow();

  var cell1 = row.insertCell();
  var cell2 = row.insertCell();
  var cell3 = row.insertCell();
  var cell4 = row.insertCell();
  var cell5 = row.insertCell();
  var cell6 = row.insertCell();

  cell1.innerHTML = "Hello";
  cell2.innerHTML = "Hello";
  cell3.innerHTML = "Hello";
  cell4.innerHTML = "Hello";
  cell5.innerHTML = "Hello";
  cell6.innerHTML = "Hello";
}

let button = document.getElementById("go-button");
let form = document.getElementById("trader-form");

button.addEventListener("click", function () {
  if (form.style.display === "none") {
    form.style.display = "flex";
  } else {
    form.style.display = "none";
  }
});
