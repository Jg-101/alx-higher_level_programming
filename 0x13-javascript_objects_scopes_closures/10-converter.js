#!/usr/bin/node
// convs a num from base 10 to another base passed as argument.

exports.converter = function (base) {
  return function (n) {
    return (n.toString(base));
  };
};
