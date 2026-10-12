
console.log("Q3:");

let productPrice = 499;
let customerMoney = 500;

// Check whether customer can buy the product
console.log(customerMoney >= productPrice); // true

// Check whether change will be left
console.log(productPrice < customerMoney); // true

if (customerMoney >= productPrice) {
    console.log("Customer can buy the product.");

    if (productPrice < customerMoney) {
        console.log("Change left: ₹" + (customerMoney - productPrice));
    }
} else {
    console.log("Customer cannot buy the product.");
}