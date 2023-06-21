// 'hi'+'hello'

// const name = 'John';
// const another = `Hi ${name}, How are you?`;
// console.log(another);

// //Exercise
// //Address object

// let Address = {
//     street : 'a',
//     city : 'b',
//     zipcode : 'c'
// }

// function showAddress(Address){
//     for(let key in Address)
//     console.log(key, Address[key])
// }

// showAddress(Address);

//Factory and construction function

// let address = createAddress('a','b','c');
// console.log(address);

// function createAddress(street, city, zipcode){
//     return{street, city, zipcode};
// }

// function Address(street, city, zipcode){
//     this.street = street;
//     this.city = city;
//     this.zipcode = zipcode;
// }

// let addres = new Address('a', 'b', 'c');


//object equality

// let address1 = new Address ('a', 'b', 'c');
// let address2 = new Address ('a', 'b', 'c');

// console.log(areEqual(address1, address2));
// console.log(areSame(address1, address2));
 
// function Address(street, city, zipcode){
//     this.street = street;
//     this.city = city;
//     this.zipcode = zipcode;
// }

// function areEqual(address1, address2){
//     return address1.street == address2.street && 
//     address1.city == address2.city &&
//      address1.zipcode == address2.zipcode;
// }

// function areSame(address1, address2){
//     return address1 === address2;
// }

//Blog post

// let post = {title:'a', body:'b', author:'c', views:'10', comments:[{author:'a',body:'b'}, {author:'c', body:'d'},], isLive:true};

// console.log(post);

//constructor functions
// let post = new Post('a','b','c');
// console.log(post);

// function Post(title,body,author){
//     this.title = title;
//     this.body = body;
//     this.author = author;
//     this.views = 0;
//     this.comments = [ ];
//     this.isLive = false;
// }

//price range objects

let priceRanges = [
    {label:'$', tooltip:'InExpensive', minPerPerson:0, maxPerPErson:10},
    {label:'$', tooltip:'Modearte', minPerPerson:11, maxPerPErson:20},
    {label:'$', tooltip:'Expensive', minPerPerson:21, maxPerPErson:50},
];

let restaurents = [ {averagePerPerson:5}];
console.log(restaurents);
