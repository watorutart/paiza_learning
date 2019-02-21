//JavaScriptの標準入力
//Node.jsを使っている？

process.stdin.resume();
process.stdin.setEncoding('utf8');

var input_string = "";
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
reader.on('line',(line) => {
    input_string = line;
});
reader.on('close',() => {
    //var input_int = parseInt(input_string);
    //var result = input_int + 100;
    //console.log(result);
    console.log("hello " + input_string);
});
