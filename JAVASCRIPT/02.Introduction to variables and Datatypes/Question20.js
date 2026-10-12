// Unique identifier: Symbol
const id1 = Symbol("id");
const id2 = Symbol("id");
console.log(typeof id1, id1 === id2); // symbol false

// Large integer with exact precision: BigInt
const exactLargeInteger = 9007199254740993n;
console.log(typeof exactLargeInteger, exactLargeInteger); // bigint 9007199254740993n

// Declared but not assigned: undefined
let notAssignedYet;
console.log(typeof notAssignedYet, notAssignedYet); // undefined undefined

// Intentional empty value: null
const emptyValue = null;
console.log(emptyValue, typeof emptyValue); // null object