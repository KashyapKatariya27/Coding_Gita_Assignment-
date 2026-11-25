
let present = true;
let internalMarks = 35;
let externalMarks = 40;

if (present == true) {
    if (internalMarks >= 30) {
        if (externalMarks >= 35) {
            console.log("Eligible for Final Exam");
        } else {
            console.log("External Marks Not Sufficient");
        }
    } else {
        console.log("Internal Marks Not Sufficient");
    }
} else {
    console.log("Student is Absent");
}
