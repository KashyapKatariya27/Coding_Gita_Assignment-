/*
a) Primitive values are simple, immutable values. Non-primitive values,
   such as objects, can store collections of data and can be changed.
   Object variables refer to an object.

b) Number, String, Boolean, undefined, null, Symbol, and BigInt are
   JavaScript's primitive types. They represent individual values and
   are not objects. (typeof null returns "object", but null is still primitive.)

c) An object is a non-primitive type. It can group related properties
   and its properties can be changed.
*/

const age = 20; // Primitive
const person = { name: "Alex", age: 20 }; // Non-primitive object

person.age = 21; // Objects can be changed
console.log(person);