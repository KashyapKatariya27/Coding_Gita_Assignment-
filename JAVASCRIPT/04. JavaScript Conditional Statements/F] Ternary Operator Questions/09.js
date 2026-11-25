let role = "admin";
let action = "delete";

let result = role == "admin"
    ? (action == "delete"
        ? "Admin Delete"
        : action == "edit"
            ? "Admin Edit"
            : "Admin Other")
    : role == "user"
        ? (action == "view"
            ? "User View"
            : "User Restricted")
        : "Invalid Role";

console.log(result);
