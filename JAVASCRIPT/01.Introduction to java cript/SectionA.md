# Section A: Short Answer Questions (1 Mark each)

**Q1. What is JavaScript?**

**Answer:** JavaScript is a lightweight, interpreted (or JIT-compiled) high-level programming language used to make web pages interactive and dynamic. It runs in the browser and also outside it (via Node.js).

---

**Q2. Who created JavaScript and in which year?**

**Answer:** JavaScript was created by **Brendan Eich** in **1995**, while he was working at Netscape.

---

**Q3. What was the original name of JavaScript?**

**Answer:** Its original name was **Mocha**. It was later renamed **LiveScript**, and finally **JavaScript**.

---

**Q4. Is JavaScript the same as Java? Give one major difference.**

**Answer:** No, they are completely different languages. Java is a statically-typed, compiled language mainly used for enterprise and Android apps. JavaScript is a dynamically-typed, interpreted language mainly used for web development.

---

**Q5. What does it mean when we say JavaScript is a high-level programming language?**

**Answer:** A high-level language is closer to human language and far from machine code. You don't need to manage memory manually or write binary/assembly. The engine handles those low-level details for you.

---

**Q6. Is JavaScript a compiled language or an interpreted language? Explain briefly.**

**Answer:** JavaScript is mainly an **interpreted** language: the JS engine reads and executes code line by line. However, modern engines like V8 use **JIT (Just-In-Time) compilation**, converting code to machine code at runtime for speed. So it is traditionally classified as interpreted, though technically it is a mix.

---

**Q7. Name the JavaScript engines used by the following browsers.**

**Answer:**
- Google Chrome → **V8**
- Mozilla Firefox → **SpiderMonkey**
- Apple Safari → **JavaScriptCore (Nitro)**

---

**Q8. What is Dynamic Typing in JavaScript?**

**Answer:** Dynamic typing means you don't declare a variable's data type explicitly. The type is decided automatically at runtime, and a variable can hold different types of values at different times.

```javascript
let x = 10;      // x is a number
x = "hello";     // now x is a string, no error
```

---

**Q9. What is the main difference between a static website and a dynamic website?**

**Answer:**
- **Static website:** Content is fixed and the same for every user. It is built with plain HTML/CSS and changes only when the developer edits the code.
- **Dynamic website:** Content changes based on user interaction, database data, or server response (e.g., a logged-in dashboard, a social media feed).

---

**Q10. Name the three pillars of Front-end Web Development and write one line about each.**

**Answer:**
1. **HTML**: provides the structure/skeleton of the webpage.
2. **CSS**: handles styling and visual presentation (colors, layout, fonts).
3. **JavaScript**: adds behavior and interactivity (click events, animations, logic).

---

**Q11. What is the difference between Frontend and Backend?**

**Answer:**
- **Frontend:** Everything the user sees and interacts with directly in the browser (UI, buttons, forms).
- **Backend:** The server-side logic, database, and infrastructure that processes requests and sends data to the frontend.

---

**Q12. What is Node.js?**

**Answer:** Node.js is a **runtime environment** that lets you run JavaScript **outside the browser** (e.g., on a server). It is built on Chrome's V8 engine and is used for backend development, file handling, servers, etc.

---

**Q13. Explain ECMAScript. What is its relation with JavaScript?**

**Answer:** ECMAScript (ES) is the **standard/specification** that JavaScript is based on. JavaScript is an **implementation** of ECMAScript. Think of ECMAScript as the rulebook and JavaScript as a language that follows those rules. Versions like ES5, ES6/ES2015
