// Complete the solution so that it reverses the string passed into it.

// 'world'  =>  'dlrow'
// 'word'   =>  'drow'

function solution(str){
  let newstr ="";
  for (let i = str.length - 1; i >= 0; i-- ) {
    newstr += str[i];
  }
  return newstr;
}

function solution(str){
  return str.split("").reverse().join("");
}


console.log(solution('world'));
console.log(solution('word'))
