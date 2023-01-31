let peticion_alta = new XMLHttpRequest();

function enter_movement(event) {
  event.preventDefault();

  const currency_to_trade = document.getElementById("currency-from");
  const quantity_to_trade = document.getElementById("quantity-from");
  const currency_desired = document.getElementById("currency-to");
  const quantity_to_obtain = document.innerHTML("quantity-to").value;

  peticion_alta.open("POST", "http://localhost:5000/api/v1/movement", true);
  peticion_alta.onload = peticion_alta_handler;
  peticion_alta.onerror = function () {
    alert("There was an error");
  };
  peticion_alta.setRequestHeader("Content-Type", "application/json");
}
