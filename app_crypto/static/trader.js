let create_request = new XMLHttpRequest();
// const transaction_request = new XMLHttpRequest();

// Function to show/hide form
let button = document.getElementById("go-button");
let form = document.getElementById("trader-form");

button.addEventListener("click", function () {
  if (form.style.display === "none") {
    form.style.display = "flex";
  } else {
    form.style.display = "none";
  }
});

// Function to connect with CoinAPI
async function getTransactionHistory() {
  const data = await fetch("http://localhost:5000/api/v1/all");
  return data.json();
}

// Function to fill content to the table
async function renderTableHistory() {
  const table_data = await getTransactionHistory();
  console.log("data", table_data);
  if (table_data) {
    const table = document.getElementById("trading-table");
    const movements = table_data.data;

    for (let i = 0; i < movements.length; i++) {
      var row = table.insertRow();

      var cell1 = row.insertCell();
      var cell2 = row.insertCell();
      var cell3 = row.insertCell();
      var cell4 = row.insertCell();
      var cell5 = row.insertCell();
      var cell6 = row.insertCell();

      cell1.innerHTML = movements[i].date;
      cell2.innerHTML = movements[i].time;
      cell3.innerHTML = movements[i].currency_from;
      cell4.innerHTML = movements[i].quantity_from;
      cell5.innerHTML = movements[i].currency_to;
      cell6.innerHTML = movements[i].quantity_to;
    }
  }
}

// Function that handles form
//pending

// Function to registrer data from transaction form
function registerTransaction(event) {
  event.preventDefault();

  const currency_available = document.getElementById("currency_to");
  const quantity_available = document.getElementById("quantity-from");
  const currency_desired = document.getElementById("currency_from");
  const quantity_to_obtain = document.getElementById("quantity-to");

  if (quantity_available === "0" || quantity_available === "") {
    alert("Debes agregar una cantidad inicial.");
  }
  create_request.open("POST", "http://localhost:5000/api/v1/new");
  create_request.onload = create_request_handler;
  create_request.onerror = function () {
    alert("No se ha podido ingresar la transacción");
    create_request.setRequestHeader("Content-Type", "application/json");
  };
}

window.onload = function () {
  renderTableHistory();
};
