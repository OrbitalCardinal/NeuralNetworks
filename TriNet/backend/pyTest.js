var spawn = require('child_process').spawn;

var input = "";
for(var i=0; i<10;i++) {
    input += i.toString() + " ";
}

var python = spawn('python', ["pyTest.py", input]);

python.stdout.on('data', (data) => {
    console.log(data.toString());
});
// console.log(input);
// python.stderr.on("data", (data) => {
//     console.log(data.toString());
//     console.log("");
// })