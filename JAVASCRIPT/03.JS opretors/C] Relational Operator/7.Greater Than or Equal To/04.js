console.log("Q4:");

console.log("25" >= 25);  // true
console.log("10" >= "2"); // false
console.log(null >= 0);   // true

// Explanation:
// "25" is converted to number 25.
// 25 >= 25 => true

// Both "10" and "2" are strings.
// They are compared lexicographically.
// "1" comes before "2", so => false

// null is converted to 0.
// 0 >= 0 => true