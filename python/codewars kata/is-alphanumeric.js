
function isAlphanumeric(string) {
  let code;

  for (let i = 0; i < string.length; i++) {
    code = string.charCodeAt(i);
    if (!(code > 47 && code < 58) &&
        !(code > 64 && code <91) &&
        !(code > 96 && code <123)) {
        return false;
        }
      }
  return true;
}

console.log(isAlphanumeric('text'));



// console.log(pigIt('Pig latin is cool'));
// //console.log(pigIt('Hello world !'));