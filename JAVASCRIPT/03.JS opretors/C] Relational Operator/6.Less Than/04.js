
console.log("Q4:");

console.log("8" < 10);      // true
console.log("20" < "3");    // true
console.log("hello" < 5);   // false

// Explanation:
// "8" < 10
// "8" is converted to number 8.
// 8 < 10 => true

// "20" < "3"
// Both are strings, so they are compared lexicographically.
// "2" comes before "3", so the result is true.

// "hello" < 5
// "hello" is converted to NaN.
// NaN < 5 => false