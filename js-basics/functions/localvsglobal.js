//Local vs Global scope

const color = 'red';

function start () {
    const msg = 'hi';
    const color ='blue';
    console.log(color);
}

function stop() {
    const msg = 'bye';
}
start();

//Let vs Var

var color = 'red'; //it is attached to window object
let age = '30'; // it is not atteched to window object

//This keyword

// const vedio = {
//     title : 'a',
//     tags : ['a', 'b','c'],

//     showTags() {
//         this.tags.forEach(function(tag) {
//             console.log(this.title.tag);
//         }, this);
//     }
// };

// vedio.showTags();

const vedio = {
    title : 'a',
    tags : ['a', 'b','c'],

    showTags() {
        this.tags.forEach(tag => {
            console.log(this.title, tag);
        });
    }
};

vedio.showTags();