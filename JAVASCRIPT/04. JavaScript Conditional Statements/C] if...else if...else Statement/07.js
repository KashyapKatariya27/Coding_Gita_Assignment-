
let units = 120;
let bill;

if (units >= 0 && units <= 50) {
    bill = units * 2;
}
else if (units <= 150) {
    bill = units * 4;
}
else {
    bill = units * 6;
}

console.log("Total Electricity Bill = Rs.", bill);
