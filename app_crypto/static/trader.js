//let create_request = new XMLHttpRequest();
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

// Function that registres the transaction and send it through POST
async function registerMovement() {
  const currencyFrom = document.getElementById("currency-from").value;
  const quantityFrom = document.getElementById("quantity-from").value;
  const currencyTo = document.getElementById("currency-to").value;
  const quantityTo = document.getElementById("quantity-to").value;

  try {
    const response = await fetch("http://localhost:5000/api/v1/new", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        currency_from: currencyFrom,
        quantity_from: quantityFrom,
        currency_to: currencyTo,
        quantity_to: quantityTo,
      }),
    });

    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

window.onload = function () {
  renderTableHistory();

  document
    .getElementById("confirm-button")
    .addEventListener("click", registerMovement);
};
