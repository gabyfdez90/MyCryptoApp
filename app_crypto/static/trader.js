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
  const currency_from = document.getElementById("currency-from").value;
  const quantity_from = document.getElementById("quantity-from").value;
  const currency_to = document.getElementById("currency-to").value;
  const quantity_to = document.getElementById("quantity_to").value;
  console.log(currency_to);
  try {
    const response = await fetch("http://localhost:5000/api/v1.0/new", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        currency_from: currency_from,
        quantity_from: quantity_from,
        currency_to: currency_to,
        quantity_to: quantity_to,
      }),
    });

    if (response.status === 201) {
      alert("La transacción ha sido registrada");
    } else {
      alert("Un error ocurrió durante el registro.");
    }
  } catch (error) {
    alert("El registro de movimiento falló.");
  }
}

window.onload = function () {
  renderTableHistory();

  document
    .getElementById("confirm-button")
    .addEventListener("click", registerMovement);
};
