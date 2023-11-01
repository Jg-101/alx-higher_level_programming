#!/usr/bin/node
// searches the second biggest int in the list of args.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
