const express = require("express");
const bodyParser = require("body-parser");
const app = express();
var spawn = require("child_process").spawn;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use((req,res,next) => {
    res.setHeader("Access-Control-Allow-Origin","*");
    res.setHeader("Access-Control-Allow-Headers","Origin, X-Requested-With, Content-Type, Accept");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST");
    next();
});

// app.use("/api/imchar",(req,res,next) => {
//     var msg;
//     var pythonProcess = spawn("python", ["./backend/pyTest.py"]);
//     pythonProcess.stdout.on("data", (data) => {
//         res.status(200).json({
//                 message: data.toString().split("\n")[0]
//             });
//     });
// });

app.post("/api/imchar", (req,res,next) => {
    var pythonProcess = spawn("python", ["./backend/processData.py", req.body.data, req.body.dimension]);
    var dataString ;
    pythonProcess.stdout.on("data", (data) => {
        dataString = data.toString()
    });
    pythonProcess.stderr.on("data",(data) => {
        dataString = data.toString()
    })
    pythonProcess.on("close",(code) => {
        res.status(201).json({
            data: dataString
        });
    });
});

app.post("/api/trainer", (req,res,next) =>{
    var pythonProcess = spawn("python", ["./backend/saveTrainData.py", req.body.data, req.body.dimension, req.body.resultado]);
    pythonProcess.stdout.setEncoding("utf8")
    var dataString ;
    pythonProcess.stdout.on("data", (data) =>{
        dataString = data.toString()
    });
    pythonProcess.stderr.on("data", (data) =>{
        dataString = data.toString()
    })
    pythonProcess.on("close", (code) =>{
        res.status(201).json({
            resultado: dataString
        });
    });
});

module.exports = app;