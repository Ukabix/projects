///It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
// You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
// assert.strictEqual(removeChar('eloquent'), 'loquen');
// assert.strictEqual(removeChar('country'), 'ountr');
// assert.strictEqual(removeChar('person'), 'erso');
// assert.strictEqual(removeChar('place'), 'lac');
// assert.strictEqual(removeChar('ooopsss'), 'oopss');
/*
function removeChar(str){
  str = str.split("");
  //console.log(str);
  str.pop();
  //console.log(str);
  str.shift();
  //console.log(str);
  str = str.join("");
  return str;
 };
/*
function removeChar(str){
  str = str.split("");
  str.splice(0,1,"");
  str.splice(str.length-1,1,"");
  str = str.join("");
  return str;
};
*/

// slice!
function removeChar(str){
  return str.split("").slice(1,str.length-1).join("");
};


console.log(removeChar("eloquent"));

console.log(removeChar('country'));
console.log(removeChar('person'));
console.log(removeChar('ooopsss'));
