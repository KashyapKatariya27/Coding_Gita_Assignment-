let maxBooks = 10;
let currentBooks = 10;

console.log("Q6:", currentBooks <= maxBooks);
// Output: true

// Important:
// currentBooks <= maxBooks is true,
// but because the bag already has exactly 10 books,
// another book cannot be added.

if (currentBooks < maxBooks) {
    console.log("More books can be added.");
} else {
    console.log("No more books can be added.");
}