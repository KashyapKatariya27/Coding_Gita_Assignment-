let a = 10;
let b = 25;
let c = 15;

let greatest = a > b
    ? (a > c ? a : c)
    : (b > c ? b : c);

console.log("Greatest Number =", greatest);
