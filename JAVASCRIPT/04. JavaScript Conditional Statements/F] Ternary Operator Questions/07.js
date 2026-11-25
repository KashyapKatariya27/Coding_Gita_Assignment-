let number = -7;

let result = number == 0
    ? "Zero"
    : number > 0
        ? (number % 2 == 0 ? "Positive Even" : "Positive Odd")
        : (number % 2 == 0 ? "Negative Even" : "Negative Odd");

console.log(result);
