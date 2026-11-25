
let cartTotal = 2000;
let premiumMember = true;
let discount;
let finalAmount;

if (cartTotal >= 1000) {
    if (premiumMember == true) {
        discount = cartTotal * 20 / 100;
    } else {
        discount = cartTotal * 10 / 100;
    }

    finalAmount = cartTotal - discount;

    console.log("Discount =", discount);
    console.log("Final Amount =", finalAmount);
} else {
    console.log("No Discount");
    console.log("Final Amount =", cartTotal);
}
