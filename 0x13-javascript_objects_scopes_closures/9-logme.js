#!/usr/bin/node
// prints the num of args already printed and the new arg val.

let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
