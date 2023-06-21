const circle = {
    radius : 1,
    draw() {
        console.log('draw');
    }
};

const another = { ...circle};
// const another = Object.assign({} , circle);

console.log(another);
