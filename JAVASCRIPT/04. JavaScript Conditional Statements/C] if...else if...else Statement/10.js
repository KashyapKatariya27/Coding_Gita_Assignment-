
let number = -7;

if (number == 0) {
    console.log("Zero");
}
else if (number > 0 && number % 2 == 0) {
    console.log("Positive Even");
}
else if (number > 0 && number % 2 != 0) {
    console.log("Positive Odd");
}
else if (number < 0 && number % 2 == 0) {
    console.log("Negative Even");
}
else {
    console.log("Negative Odd");
}
