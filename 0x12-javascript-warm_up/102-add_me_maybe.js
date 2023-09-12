#!/usr/bin/node
// execs x times a func.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
