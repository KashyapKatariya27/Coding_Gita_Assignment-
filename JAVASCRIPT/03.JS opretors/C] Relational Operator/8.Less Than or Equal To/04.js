console.log("Q4:");

console.log("15" <= 20);  // true
console.log("30" <= "5"); // true
console.log(null <= 0);   // true

// Explanation:
// "15" is converted to number 15.
// 15 <= 20 => true

// "30" and "5" are both strings.
// They are compared lexicographically.
// "3" comes before "5", so => true

// null converts to 0.
// 0 <= 0 => true