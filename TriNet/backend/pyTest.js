var spawn = require('child_process').spawn;

var python = spawn('python', ["pyTest.py"]);

python.stdout.on('data', (data) => {
    console.log(data.toString());
});
// console.log(input);
// python.stderr.on("data", (data) => {
//     console.log(data.toString());
//     console.log("");
// })