let age = 25;
let graduation = true;
let experience = 3;

if (age >= 21 && age <= 30) {
    if (graduation == true) {
        if (experience >= 2) {
            console.log("Eligible for Interview");
        } else {
            console.log("Not Enough Experience");
        }
    } else {
        console.log("Graduation Degree Required");
    }
} else {
    console.log("Age Criteria Not Satisfied");
}
