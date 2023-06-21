//Spread operator
const first = [1,2,3];
const second = [4,5,6];

const combined = [...first, 'a', ...second,'b'];
const copy = [...combined];

console.log(copy);

//Iterating an array

const numbers = [1,2,3];
for(let number of numbers)
    console.log(number);

// numbers.forEach(function(numbers){
//     console.log(numbers)});

numbers.forEach(numbers => console.log(numbers));
