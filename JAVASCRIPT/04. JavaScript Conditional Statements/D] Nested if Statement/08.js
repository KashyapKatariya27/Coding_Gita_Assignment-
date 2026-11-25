
let number = 12;

if (number > 0) {
    if (number % 2 == 0) {
        if (number % 4 == 0) {
            console.log("Positive Even and Divisible by 4");
        } else {
            console.log("Positive Even but Not Divisible by 4");
        }
    } else {
        console.log("Positive Odd Number");
    }
} else {
    console.log("Number is Not Positive");
}
