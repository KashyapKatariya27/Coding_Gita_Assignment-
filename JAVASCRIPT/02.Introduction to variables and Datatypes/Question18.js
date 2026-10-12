const symbol1 = Symbol("id");
const symbol2 = Symbol("id");

console.log(symbol1 === symbol2); // false

const values = {
  [symbol1]: "Value for symbol1",
  [symbol2]: "Value for symbol2",
};

console.log(values[symbol1]); // Value for symbol1
console.log(values[symbol2]); // Value for symbol2