//Arrow functions
const courses = [ 
    {id:1, name:'a'},
    {id:2, name:'b'},
];

const Courses = courses.find(course => course.name === 'a');
console.log(Courses);

//Removing elements

const numbers = [1,2,3,4,5];
const last = numbers.pop(); 
const first = numbers.shift();
const middle = numbers.splice(2,2);
console.log(numbers);

//Emptying an array

let numbers = [1,2,3,4];
let another = numbers;

// numbers = [];
numbers.length = 0;
// numbers.splice(0, numbers.length);
// while(numbers.length>0)
//     numbers.pop();
console.log(numbers);
console.log(another);

//Combining and slicing arrays

const first = [{id:1}];
const second = [4,5,6];

const Combined = first.concat(second);
first[0],id =10;
const slice = Combined.slice();
console.log(Combined);
console.log(slice);