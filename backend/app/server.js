const express = require("express");

const app = express();

app.use(express.json());

app.get("/hello", (req, res) => {
    const name = req.query.name;

    // Issue: user input directly inserted into HTML
    res.send("<h1>Hello " + name + "</h1>");
});

app.post("/admin/delete", (req, res) => {
    const user = req.body.user;

    // Issue: no authentication/authorization
    console.log("Deleting user:", user);

    res.json({
        message: "User deleted",
        user: user
    });
});

app.listen(3000);
