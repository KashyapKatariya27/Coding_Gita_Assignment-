
let pin = 1234;
let enteredPin = 1234;
let balance = 5000;
let withdraw = 2000;

if (enteredPin == pin) {
    if (withdraw <= balance) {
        balance = balance - withdraw;
        console.log("Withdrawal Successful");
        console.log("Remaining Balance =", balance);
    } else {
        console.log("Insufficient Balance");
    }
} else {
    console.log("Incorrect PIN");
}
