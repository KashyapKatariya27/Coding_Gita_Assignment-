# Question 9 : Predicted Output & Explaination 

---

**Predicted Output :** 20, then a ReferenceError on console.log(y)

## Explaination : 

- var x is function/global scoped and can be re-declare.The var x = 20 inside the if is the same variable as the outer x, so it overwrites 10. That's why x print 20.

- let y is block-scoped, so it exists only inside the if block . Accessing it outside gives a ReferenceError.

- conset z is also block-scoped, so console.log(z) would give the same ReferenceError.It is never reached because the program stops at the y error.


