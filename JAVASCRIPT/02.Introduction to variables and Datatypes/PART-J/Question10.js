// a) Objects store named properties. Arrays store ordered lists of items.
const person = { name: "Riya", age: 18 };
const colors = ["red", "green", "blue"];
console.log("Object:", person);
console.log("Array:", colors);

// b) typeof null returns "object" because of an old JavaScript behavior.
// null means no value; it is not actually an object.
const emptyValue = null;
console.log("typeof null:", typeof emptyValue);

// c) Arrays with one data type are easier to understand and use.
const numbers = [3, 1, 2];
console.log("Numbers:", numbers);

// d) Use const when you will not reassign a variable, and let when you will.
const name = "Riya";
let score = 0;
score = 10;
console.log("Name:", name);
console.log("Score:", score);
