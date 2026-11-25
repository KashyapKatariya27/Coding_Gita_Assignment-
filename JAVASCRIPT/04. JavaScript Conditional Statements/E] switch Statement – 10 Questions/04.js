let marks = 85;

switch (true) {
    case (marks >= 75):
        console.log("Distinction");
        break;

    case (marks >= 60):
        console.log("1st Class");
        break;

    case (marks >= 50):
        console.log("2nd Class");
        break;

    case (marks >= 35):
        console.log("3rd Class");
        break;

    default:
        console.log("Failed");
}
