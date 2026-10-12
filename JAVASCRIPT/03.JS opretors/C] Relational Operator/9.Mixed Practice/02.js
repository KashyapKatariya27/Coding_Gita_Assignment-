console.log("Q2:");

console.log(10 > 5 && 5 < 10);
// true
// 10 > 5 => true
// 5 < 10 => true
// true && true => true


console.log("10" >= 10);
// true
// "10" is converted to number 10.
// 10 >= 10 => true


console.log(null <= undefined);
// false
// undefined becomes NaN during relational comparison.
// Comparison with NaN => false


console.log("5" < "10" && 5 > 2);
// false
// "5" < "10" => false because both are strings.
// They are compared lexicographically.
// 5 > 2 => true
// false && true => false