const express = require("express");
const bodyParser = require("body-parser");
const app = express();

app.use((req,res,next) => {
    res.setHeader("Access-Control-Allow-Origin","*");
    res.setHeader("Access-Control-Allow-Header","Origin, X-Requested-With, Content-Type, Accept");
    res.setHeader("Access-Control-Allow-Methods", "GET, OPTIONS");
    next();
});

app.use("/api/imchar",(req,res,next) => {
    res.status(200).json({
        message:  "Increible"
    });
});

module.exports = app;