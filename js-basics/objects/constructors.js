// function createCircle(radius){
//     return{
//         radius,
//         draw(){
//             console.log('draw');
//         }
//     };
// }

// const myCircle = createCircle(1);

// function Circle(radius){
//     this.radius = radius;
//     this.draw = function(){
//         console.log('draw');
//     }
// }

// const myCircle2 = new Circle(1);

function createCircle(radius){
    return {
        radius,
        draw(){
            console.log('draw');
        }
    };
}

const myCircle = createCircle(1);

function Circle(radius){
    this.radius = radius;
    this.draw = function(){
        console.log('draw');
    };
}

const myCircle2 = new Circle(1);
console.log(myCircle2)