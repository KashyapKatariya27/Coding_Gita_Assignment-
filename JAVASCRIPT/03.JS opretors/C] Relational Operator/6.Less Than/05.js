console.log("Q5:");

console.log(null < 0);       // false
console.log(undefined < 0);  // false

// Explanation:
// null converts to 0.
// 0 < 0 => false

// undefined converts to NaN.
// NaN < 0 => false