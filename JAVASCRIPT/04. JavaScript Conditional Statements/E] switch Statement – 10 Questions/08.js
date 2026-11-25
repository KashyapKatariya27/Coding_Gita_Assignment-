let num1 = 10;
let num2 = 3;
let operator = "**";
let result;

switch (operator) {
    case "+":
        result = num1 + num2;
        console.log("Result =", result);
        break;

    case "-":
        result = num1 - num2;
        console.log("Result =", result);
        break;

    case "*":
        result = num1 * num2;
        console.log("Result =", result);
        break;

    case "/":
        if (num2 == 0) {
            console.log("Cannot divide by zero");
        } else {
            result = num1 / num2;
            console.log("Result =", result);
        }
        break;

    case "%":
        if (num2 == 0) {
            console.log("Cannot divide by zero");
        } else {
            result = num1 % num2;
            console.log("Result =", result);
        }
        break;

    case "**":
        result = num1 ** num2;
        console.log("Result =", result);
        break;

    default:
        console.log("Invalid Operator");
}


// Output :

//Result = 1000