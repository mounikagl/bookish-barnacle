//joining arrays
const numbers = [1,2,3];
const joined = numbers.join(',');
console.log(joined);

const message = 'This is my frist message';
const parts = message.split(' ');
console.log(parts);

const combined = parts.join('-');
console.log(combined);

//sorting arrays

const courses = [
    {id:1, name:'Node.js'},
    {id:2, name:'JavaScript'},
];

courses.sort(function(a,b){
    const nameA = a.name.toLowerCase();
    const nameB = b.name.toLowerCase();

    if (nameA < nameB) return -1;
    if (nameA > nameB) return 1;
        return 0;
}
);

console.log(courses);

//Testing the elements of an array

const courses =[1,-1,2,3];

// const atLeastOnePositive = courses.some(function(values){
const atLeastOnePositive = courses.every(function(values){

    return values >= 0;
}
);

console.log(atLeastOnePositive);

//filtering an array

const numbers = [1,-1,2,3];

const filtered = numbers.filter(n => n >= 0);
console.log(filtered);

//Mapping an array

const numbers = [1,2,3];
// const filtered = numbers.filter(n => n >= 0);
// const items = filtered.map(n => ({value:n}));

const items = numbers
.filter(n => n >= 0)
.map(n => ({value:n}))
.filter(obj => obj.value>1)
.map(obj => obj.value)

console.log(items);


//Reducing an array

const numbers = [1,-1,2,3];
const sum = numbers.reduce(
    (accumulator, cuurentValue) => accumulator + cuurentValue);

console.log(sum);

