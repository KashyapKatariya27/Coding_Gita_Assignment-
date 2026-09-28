# Section A : Short Answer Question
---


**(Q1)** What Is JavaScript?

-> JavaScript is a lightweight, interpretend(or JIT-compiled) high-level programming languge used to make web pages 
   interactive and dynamic. it euns in the browser and also outside it (via Node.js).

**(Q2)** Who Created JavaScript and in which year?

-> JavaScript was Created by Brendan Eich in 1995, while he was working at Netscape.

**(Q3)** What was the original name of JavaScript?

-> Its original name was Mocha, later renamed to LiveScript, and finally JavaScript.

**(Q4)** is JavaScript the same as Java? Give one major difference.

-> No, JavaScript and java are completely different languges.Major difference: Java is a statically-typed, compiled languge 
   mainly used for enterprice/android apps,while javascript is a dynamically-typed, interpretend languge mainly used for 
   web-development.

**(Q5)** What does it mean when we say JavaScript is a high-level programming languge?

-> A high-level languge means it's closer to human languge and far from machine code-you don't need to manage memory manually
  (like allocating/freeing memory) or write in binary/assembly.The engine handles those low-level details fo you.

**(Q6)** is JavaScript a compiled languge or an interpretend languge? Explain briefly.

-> javascript is mainly an interpretend languge-the JS engine reads and executes code line by line.However, morden engine(like v8)
   use JIT(Just-In-Time) compilation,converting code to machine code at runtime for speed.so technically it's a mix,but it'same
   traditionally classified as interpretend.

**(Q7)** Name the JavaScript engines used by the following browser:
   
   . Google Chrome --> V8

   . Mozilla Firefox--> SpiderMonkey

   . Apple Safari--> JavaScriptCore(Nitro)

**(Q8)** What is Dynamic Typing in JavaScript?

-> Dynamic Typing means you don't need to declare a variable's data type explicitly -the type is determined automatically at 
   runtime,and a variable can hold different types of values at different times.

   '''JavaScript                    
   let x = 10;                   
   x = "hello";     
   '''            
   

**(Q9)** What is the main difference between a static website and dynamic website?

-> **Static website:** Content is fixed and same for every user; built with plain HTML/CSS,doesn't change unless the developer edits
   the code.

   **Dynamic website:** Content can change based on user interaction, database data,or server response (e.g.., a logged-in-dashboard,
   social media feed).

**(Q10)** Name the three pillars of Front-web Web Deplyonment and write one line about each.

->  **HTML** - provides the structure/skeleton of the webpage.

**CSS** - handles styling and visual presentation (colors,layout,fonts).

**JavaScript** - adds behavior and interactivity (click events,animations,logic).

**(Q11)** What is the difference between Frontend and Backend?

->  **Frontend:** Everything the user sees and interacts with directly in the browser(UI,buttons,forms).

**Backend:** The server-side logic,database,and infrastructure that processes request and sends data to the frontend.

**(Q12)** What is Node.js?

->  Node.js is a **runtime environment** that lets you run javaScript outside the browser(e.g., development,file handling,
    server,etc.)

**(Q13)** Explain ECMAScript. What is its relation with Javascript?

->  ECMAScript (ES) is the standerd/specification that javascript is based on.javaScript is an implementation of ECMAScript-
    think of ECMAScript as the rulebook,and javaScript as one languge that follows those rules(version like ES5,ES6/ES2015,ES2020
    etc.define new features JS adopts). 

---    

## Section B: True or False
---

(Q1) Javascript is a statically typed languge.

--> False -> JavaScript is a **dynamically** typed languge.

(Q2) javaScript can only run inside the browser.

--> False -> JavaScript can run outside the browser too (e.g., using Node.js)

(Q3) HTMl is responseible for the behaviour of a webpage.

--> False -> CSS(not HTML) is responsible for the behaviour... actually correction:

   HTMl is responsible for structure,not behavior.Behaviour is handled by JavaScript.

(Q4) Node.Js allows javaScript to run outside the browser .

--> True

(Q5) JavaScript is case-insensitive.

--> False -> JavaScript is **case-sensitive.**

(Q6) let name and let Name are the same variable.

--> False -> 'let name' and 'let Name' are different variable (case-sensitive).

(Q7) ECMAScript is a programming languge.

--> False -> ECMAScript is a **specification/standerd**,not a programming languge itself.

(Q8) React,Angular, and Vue.js are used for Backend development.

--> False -> React,Angular,and Vue.js are used for Frontend development.

# Section C: Fill in the Blanks
--- 


(1) JavaScript was Created by **Brendan Eich** in the year **1995**.

(2) the three technologies used in Front-end developmement are **HTML**,**CSS**,**JavaScript.**

(3) JavaScript engines: chrome uses **V8**, firefox uses **Spidermonkey.**

(4) In the resturent analogy: Customer = **User/Browser (Frontend)**,waiter = **Server/API**, Chef = **Backend/Database.**

(5) JavaScript file extension is **.Js**

---

# Section D : Conceptual Question 
---

**(Q14)** Differentiate between a static website and dynamic website. Give one real-world example of each.

->  A **static website** shows the same fixed content to every visitor and doesn't interact with a database - e.g.,a simple 
    portfolio page with hardcoded HTML. A dynamic website generates or changes content based on user input,time, or database
    queries- e.g., Instagram,where your feed is Different from everyone else's and updates constantly.

**(Q15)** Explain any two features of JavaScript that makes it suitable for craating interactive web pages.

->  1. **Event handling** - JS can delect user actions like clicks,key press,or mouse movement and respond instantly(e.g.,showing a menu on click).

 2. **DOM manipulation** - JS can dyanamically change HTML content,styles,and structure without reloading the page(e.g.,
    updating a cart count when you add an item).

**(Q16)** List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each (if applicable)

-> 1.**Backend developmement** -> Node.Js.

   2.**Mobile app developmement** -> React Native

   3.**Desktop app developmement** -> Electron.Js
    
   4.**AI/Machine Learning** -> TensorFlow.Js

**(Q17)** What is the Difference between writing JavaScript code:

   - Inside an HTML file using '<script>'  tag,and 

   -> **Inline ('<script>' in HTML)**:JS code is written directly inside the HTMl file.

   . in an external .js file?
     Mention two advantage of using an external JavaScript file.

   ->External .js file:JS code is written in a separate file and linked using <script src="file.js"></script>.
   Two adavantage of external files:
   1. Reusability - the same JS file can be linked to multiple HTMl pages.
   2. Better maintaiability-keeps HTML(structure) and JS(logic)separate,making code cleaner and easier to debug/update.

**(Q18)** Explain the Difference between Frontend and Backend using the resturent analogy in your own words.

->  In a resturent analogy:YOU(the Customer) are the Frontend-you see the menu and place an order,similar to how a user
    interacts with a website's interface. The waiter is like the Backend server - they take your request,pass it to the
    kitchen,and bring the response back,similar to an API relaying request between the browser and the database.The chef 
    is like the database-they actually prepare/store the "data"(food) that gets delivered back to you.

**(Q19)** Why should a beginner learn JavaScript? Write at least 4 points.

->  1. It's the only language browsers understand Natively,making it essential for web developmement.

 2. It has huge demand in the job market for Frontend,Backend,and full-stack roles.

 3. It has a massive ecosystem - frameworks like React,Angular,Vue,and Node.js are all JS-based.

 4. It's beginner-friebdly - easy to start with,since you just need a browser ,no complex setup required.

---

# Section E : Code-Based Question 
---

**(Q20)** Predict the output of the following code and explain why:

'''javascript
let value = 25;
consel.log(typeof value);
value = "JavaScript";
consel.log(typeof value);
value = false;
consel.log(typeof value);
'''

- output :

  number

  string

  boolean

  **Explanation**: Javascript is dynamically typed,so 'typeof' returns the type of the **current value** stored in the variable at that moment - it changes as 'value' is ressigned from a number, to a string, to a boolean.

 **(Q21)** write a simple HTMl + JavaScript program that display an alert box with the message **Welcome to Javascript** when a button is '"clicked!"'.

'''html
<!DOCTYPE html>
<html>
<head>
 <title>Alert Example</title>
<head>
<body>
 <button onclick="showsAlert()">click Me</button>

 <script>
  function showAlert() {
   alert("Welcome to javascript!");
  }
 </script>
</body>
</html>
'''

**(Q22)** Write JavaScript code to demonstrate **even-driven programming**.
whwn a user clicks a button with id '"mybtn"', the text of a paragraph with id '"demo"' should change to '"button was clicked!"'.


'''html
<!DOCTYPE html>
<html>
<body>
 <button id="myBtn">Click Me</button>
 <p id = "demo">This text will change.</p>

 <script>
   document.getElementById("myBtn").addEventListener("click",function(){
      document.getelemenmtById("demo").textContent = "Button was clicked!";
   });
   </script>
  </body>
  </html>
  ''' 


  ---

  # Section F : Practical / Applicatrion Based 

  ---

  **(Q23)** create a complete web page (HTMl + JavScript) that includes the following:

  1. A heading **" My First JavaScript Page"**

  2. A button labeled **"Click Me"**

  3. When the button is clicked:
   - Show an alert: '"Hello,B.tech Student!"'
   - Chage the background color of the page to light blue

  4. Also print '"JavaScript is running successfully!"' in the browser consel.

  **Write the complete code** (you can use inline or External JavaScript).

  '''html
  <!DOCTYPE html>
  <html>
  <head>
   <tittle> My First JavaScript Page </title>
  </head>
  <body>
   <h1>My First JavaScript Page</h1>
   <button id="actionBtn">Click Me</button>

   <script>
    document.getElementById("actionBtn").addEventListener("click", function (){
      alert("Hello, B.tech student!");
      document.body.style.backgroundColor = "lightblue";
      concel.log("JavaScript is running successfully!");
     });
     </script>
   </body>
   </html>
    ''' 

   ---

