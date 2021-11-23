// You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

// #Examples:

// Kata.getMiddle("test") should return "es"

// Kata.getMiddle("testing") should return "t"

// Kata.getMiddle("middle") should return "dd"

// Kata.getMiddle("A") should return "A"

// #Input

// A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

// #Output

// The middle character(s) of the word represented as a string.

function getMiddle(word) {
  const wordArray = Array.from(word); // cast to array
  const index = Math.ceil(wordArray.length / 2);; // calculate index with ceiling (floor could be used for both, round for odds)
  if ((wordArray.length === 0)) { // handle string len === 0
    return "";
  } else if ((wordArray.length === 1)) { // handle string len === 1, before odd string with len > 1
    return "" + wordArray[0];
  } else if (wordArray.length % 2 !== 0) { // handle odd string len
    return "" + wordArray[index-1]; // since we used ceiling method, use +1 for floor
  } else { // handle even string len
    return "" + wordArray[index-1] + wordArray[index]; // use 0 and +1 for floor
  }
}

console.log(getMiddle("test"));
console.log(getMiddle("testing"));
console.log(getMiddle("middle"));
console.log(getMiddle("A"));
console.log(getMiddle("Aa"));
