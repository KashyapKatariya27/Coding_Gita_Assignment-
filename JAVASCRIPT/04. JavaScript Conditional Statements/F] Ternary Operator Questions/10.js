let cartTotal = 6000;

let result = cartTotal >= 5000
    ? { discount: "20%", finalAmount: cartTotal * 0.80 }
    : cartTotal >= 2000
        ? { discount: "10%", finalAmount: cartTotal * 0.90 }
        : cartTotal >= 1000
            ? { discount: "5%", finalAmount: cartTotal * 0.95 }
            : { discount: "0%", finalAmount: cartTotal };

console.log(result);
