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

// Function to connect with list of movements API
async function getTransactionHistory() {
  const data = await fetch("http://localhost:5000/api/v1/all");
  return data.json();
}

// Function to fill content to the table
async function renderTableHistory() {
  const table_data = await getTransactionHistory();

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

// Function to get values from trade rate API
async function getRateFromAPI() {
  let currency_from = document.getElementById("currency-from").value;
  let currency_to = document.getElementById("currency-to").value;

  const data = await fetch(
    `http://localhost:5000/api/v1/tasa/${currency_from}/${currency_to}`
  );

  return data.json();
}

//Function to fill up values in transaction from
async function addValuesForm() {
  const quantity_to_placeholder = document.getElementById("quantity-to");
  const unit_price_placeholder = document.getElementById("unit-price");
  const quantity_from_placeholder = document.getElementById("quantity-from");
  const quantity_from = quantity_from_placeholder.value;
  const data = await getRateFromAPI();

  if (data) {
    const quantity_to = data.rate * quantity_from;
    quantity_to_placeholder.value = quantity_to.toFixed(10);

    const unit_price = data.rate;
    unit_price_placeholder.value = unit_price.toFixed(10);
  }
}

//Function that cleans up the table
async function clearTable() {
  const table = document.getElementById("trading-table");
  const rowCount = table.rows.length;

  for (let i = rowCount - 1; i >= 1; i--) {
    table.deleteRow(i);
  }
}
// Function that registres the transaction and send it through POST
async function registerMovement() {
  const currencyFrom = document.getElementById("currency-from").value;
  const quantityFrom = document.getElementById("quantity-from").value;
  const currencyTo = document.getElementById("currency-to").value;
  const quantityTo = document.getElementById("quantity-to").value;
  const unitPrice = document.getElementById("unit-price").value;

  if (currencyFrom === currencyTo) {
    alert("Seleccione dos monedas diferentes.");
  }

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
        unit_price: unitPrice,
      }),
    });

    const result = await response.json();
    alert(result.message);
  } catch (error) {
    alert(result.message);
  }
  clearTable();
  renderTableHistory();
}

//Function that triggers when hit the cancel button
function cancelTransaction() {
  document.getElementById("quantity-from").value = "";
  document.getElementById("quantity-to").value = "";
  document.getElementById("unit-price").value = "";
}

// Function that get investment status from endpoint
async function getStatusFromAPI() {
  const data = await fetch("http://localhost:5000/api/v1/status");

  console.log(data);
  return data.json();
}

// Function that write investment status on screen
function writeInversionStatus() {
  let invested = document.getElementById("total-invested");
  let recovered = document.getElementById("total-recovered");
  let purchaseValue = document.getElementById("purchase-value");
  let currentAssets = document.getElementById("current-assets");

  const data = getStatusFromAPI();

  if (data) {
    invested.value = data.invested;
    recovered.value = data.recovered;
    purchaseValue.value = data.purchaseValue;
    currentAssets.value = data.currentAssets;
  }
}

window.onload = function () {
  renderTableHistory();
  writeInversionStatus();

  document
    .getElementById("confirm-button")
    .addEventListener("click", registerMovement);

  document
    .getElementById("calculate-button")
    .addEventListener("click", addValuesForm);

  document
    .getElementById("cancel-button")
    .addEventListener("click", cancelTransaction);

  document
    .getElementById("status-section")
    .addEventListener("click", writeInversionStatus);
};
