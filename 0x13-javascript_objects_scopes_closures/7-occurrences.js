#!/usr/bin/node
// func that returns the num of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(e => e === searchElement).length);
};
