let category = "veg";
let item = "paneer";
let size = "full";

let price = 0;

switch (category) {
    case "veg":
        switch (item) {
            case "paneer":
                price = 200;
                break;

            case "pizza":
                price = 250;
                break;

            default:
                console.log("Invalid Veg Item");
        }
        break;

    case "nonveg":
        switch (item) {
            case "chicken":
                price = 300;
                break;

            case "burger":
                price = 180;
                break;

            default:
                console.log("Invalid Non-Veg Item");
        }
        break;

    default:
        console.log("Invalid Category");
}

if (price > 0) {
    switch (size) {
        case "half":
            price = price / 2;
            break;

        case "full":
            break;

        default:
            price = 0;
            console.log("Invalid Size");
    }
}

if (price > 0) {
    console.log("Category =", category);
    console.log("Item =", item);
    console.log("Size =", size);
    console.log("Final Price = Rs.", price);
}


// output :

// Category = veg
// Item = paneer
// Size = full
// Final Price = Rs. 200