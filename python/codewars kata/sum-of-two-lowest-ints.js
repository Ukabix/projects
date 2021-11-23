// Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

// For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

// [10, 343445353, 3453445, 3453545353453] should return 3453455.

array = [19, 5, 42, 2, 77];

array = array.sort((a, b) => a - b);
const num1 = array[0];
const num2 = array[1];

console.log(array);
