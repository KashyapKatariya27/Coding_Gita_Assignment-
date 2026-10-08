console.log(10 / 0); // Output: Infinity => JS follows simple maths rules while executing division operator
console.log(-10 / 0); // Output: -Infinity => JS follows simple maths rules while executing division operator
console.log(0 / 0); // Output: NaN => As 0/0 is not defined in maths so JS gives NaN
console.log("20" / "4" / 2); // Output: 2.5 => JS converts string datatype into number while executing division operator
console.log("abc" / 5); // Output: NaN => As abc can't be converted to number datatype so JS will give output with type number and value Not a Number