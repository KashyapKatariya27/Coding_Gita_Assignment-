
let income = 500000;
let tax;

if (income < 300000) {
    tax = 0;
}
else if (income <= 700000) {
    tax = income * 5 / 100;
}
else if (income <= 1000000) {
    tax = income * 10 / 100;
}
else {
    tax = income * 15 / 100;
}

console.log("Tax Amount =", tax);
