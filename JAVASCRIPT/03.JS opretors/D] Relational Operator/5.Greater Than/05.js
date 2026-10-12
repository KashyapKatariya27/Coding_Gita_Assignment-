// Question 5
// null > 0 and undefined > 0

console.log("Q5:");
console.log(null > 0);       // false
console.log(undefined > 0);  // false

// Explanation:
// null is converted to 0, so 0 > 0 is false.
// undefined is converted to NaN.
// NaN > 0 is false.