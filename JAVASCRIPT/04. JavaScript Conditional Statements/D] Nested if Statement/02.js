
let age = 20;
let voterID = true;

if (age >= 18) {
    if (voterID == true) {
        console.log("Can Vote");
    } else {
        console.log("Voter ID is required");
    }
} else {
    console.log("Not Eligible to Vote");
}
