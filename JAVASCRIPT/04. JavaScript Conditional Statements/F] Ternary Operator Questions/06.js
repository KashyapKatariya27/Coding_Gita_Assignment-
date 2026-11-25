let marks = 65;

let result = marks >= 75
    ? "Distinction"
    : marks >= 60
        ? "First Class"
        : marks >= 50
            ? "Second Class"
            : marks >= 35
                ? "Pass"
                : "Fail";

console.log(result);
