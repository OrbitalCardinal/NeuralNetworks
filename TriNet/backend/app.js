const express = require("express");
const bodyParser = require("body-parser");
const app = express();
var spawn = require("child_process").spawn;

app.use((req,res,next) => {
    res.setHeader("Access-Control-Allow-Origin","*");
    res.setHeader("Access-Control-Allow-Header","Origin, X-Requested-With, Content-Type, Accept");
    res.setHeader("Access-Control-Allow-Methods", "GET, OPTIONS");
    next();
});

app.use("/api/imchar",(req,res,next) => {
    var msg;
    var pythonProcess = spawn("python", ["./backend/pyTest.py"]);
    pythonProcess.stdout.on("data", (data) => {
        res.status(200).json({
                message: data.toString().split("\n")[0]
            });
    });
});

module.exports = app;