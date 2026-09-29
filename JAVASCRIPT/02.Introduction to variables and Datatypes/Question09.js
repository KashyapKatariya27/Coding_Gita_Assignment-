var x = 10;

if (true) {
    var x = 20;    //same x, re-declared and overwritten
    let y = 30;   //block-scoped
    const z = 40; //block-scoped
}

console.log(x);  //20
console.log(y);  // ReferenceError: y is not defined
console.log(z);  // never runs, because the error above stops the program


