// We need a function that can transform a number into a string.

// What ways of achieving this do you know?
// Examples:

// 123 --> "123"
// 999 --> "999"



function toString1(string1) {
  string1 = String(string1);
  console.log(string1);
  console.log(typeof(string1));
}

function toString2(string2) {
  string2 = string2.toString();
  console.log(string2);
  console.log(typeof(string2));
}

function toString3(string3) {
  string3 += "";
  console.log(string3);
  console.log(typeof(string3));
}

toString1(123);
toString2(999);