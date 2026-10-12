console.log(a); // undefined: var is hoisted and initialized as undefined.

try {
  console.log(b);
} catch (error) {
  console.log(error.name); // ReferenceError: b is in its temporal dead zone.
}

try {
  console.log(c);
} catch (error) {
  console.log(error.name); // ReferenceError: c is in its temporal dead zone.
}

var a = 10;
let b = 20;
const c = 30;

console.log(a, b, c); // 10 20 30