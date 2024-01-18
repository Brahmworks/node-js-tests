// Sample Javascript Code to test USB Communication

const { SerialPort } = require('serialport');
const COM_PORT = 'COM4';
const BAUD = 9600;

const port = new SerialPort({ path: COM_PORT, baudRate: BAUD }, function (err) {
    if (err) {
        deviceStatus = "Not Connected";
        return console.log('Error: ', err.message)
    }
})

console.log('Creating your message');
// var message = "Hello World";
// console.log(message);

const byteArray = Buffer.from('7B7C01020101010100002000FF7C7D', 'hex');
console.log(byteArray);

// string = JSON.stringify(message);
// console.log(string);
port.write(byteArray, function (err) {
    if (err) {
        return console.log('Error on write: ', err.message)
    }
    console.log('Message Written on: ',COM_PORT);
})

