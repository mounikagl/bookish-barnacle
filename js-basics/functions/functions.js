//function declaration

function walk() {
    console.log('Walk');
}

//anonynomus function expression\

const run = function() {
    console.log('Run');
};

let move = run();
run();
move();

//hoisting

//func declaration
walk();
function walk() {
    console.log('Walk');
}

//func expression

run();
const run = function() {
    console.log('Run');
}

