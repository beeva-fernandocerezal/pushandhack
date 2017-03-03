/**
 * Created by carlos.gonzalez on 3/3/17.
 */
var async = require('async');
var example_function = require('./exampleFunction.js');
exports.handler = function(event, context, callback){
    console.log("Hola");
    callback(null, 'Hello from Lambda');
    example_function.printHello();
};
