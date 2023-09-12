#!/usr/bin/node
// func that returns the reved version of a list without reverse

exports.esrever = function (list) {
  const reversedList = [];
  const last = list.length - 1;
  for (let i = last; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};
