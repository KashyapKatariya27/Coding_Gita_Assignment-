# Section E: Code-Based Questions (3 Marks each)

**Q20. Predict the output of the following code and explain why:**

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```

**Answer:**

Output:

```
number
string
boolean
```

Explanation: JavaScript is dynamically typed, so `typeof` returns the type of the **current value** stored in the variable at that moment. As `value` is reassigned from a number (`25`) to a string (`"JavaScript"`) to a boolean (`false`), its type changes each time.

---

**Q21. Write a simple HTML + JavaScript program that displays an alert box with the message "Welcome to JavaScript!" when a button is clicked.**

**Answer:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Alert Example</title>
</head>
<body>
  <button onclick="showAlert()">Click Me</button>

  <script>
    function showAlert() {
      alert("Welcome to JavaScript!");
    }
  </script>
</body>
</html>
```

---

**Q22. Write JavaScript code to demonstrate event-driven programming. When a user clicks a button with id "myBtn", the text of a paragraph with id "demo" should change to "Button was clicked!".**

**Answer:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Event Driven Example</title>
</head>
<body>
  <button id="myBtn">Click Me</button>
  <p id="demo">This text will change.</p>

  <script>
    document.getElementById("myBtn").addEventListener("click", function () {
      document.getElementById("demo").textContent = "Button was clicked!";
    });
  </script>
</body>
</html>
```

Explanation: The code waits for a `click` event on the button and runs the function only when that event happens. This is event-driven programming.