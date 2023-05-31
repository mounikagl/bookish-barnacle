console.log(true && true);
console.log(true && false);

let highIncome = true;
let goodCreditScore = true;
let eligibleForLoan = highIncome && goodCreditScore;

console.log("Eligible", eligibleForLoan)

let applicationRefused = !eligibleForLoan;
console.log("Apllication Refused", applicationRefused);


// Anything that is not falsy is truthy.
console.log(false || true);
console.log(false || 1);
console.log(false || "Mosh");

// short circuiting
console.log(false||1||2);

// let currentColor ="Red";
let currentColor =undefined;
let userColor = "Blue";
let color = currentColor || userColor;
console.log(color);