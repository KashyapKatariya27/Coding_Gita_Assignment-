# Section F: Practical / Application Based (5 Marks)

**Q23. Create a complete web page (HTML + JavaScript) that includes the following:**

1. A heading: "My First JavaScript Page"
2. A button labeled "Click Me"
3. When the button is clicked:
   - Show an alert: "Hello, B.Tech Student!"
   - Change the background color of the page to light blue
4. Also print "JavaScript is running successfully!" in the browser console.

**Answer:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First JavaScript Page</title>
</head>
<body>
  <h1>My First JavaScript Page</h1>
  <button id="actionBtn">Click Me</button>

  <script>
    document.getElementById("actionBtn").addEventListener("click", function () {
      alert("Hello, B.Tech Student!");
      document.body.style.backgroundColor = "lightblue";
      console.log("JavaScript is running successfully!");
    });
  </script>
</body>
</html>
```

How to run: save the code as `index.html`, open it with VS Code Live Server (or double-click it), and click the button. Open the browser console (F12) to see the console message.