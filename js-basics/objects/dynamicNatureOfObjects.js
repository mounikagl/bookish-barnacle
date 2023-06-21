const Circle = {
    radius : 1
};

// Circle = {};

Circle.color = 'yellow';
Circle.draw = function() {}

delete Circle.color;
delete Circle.draw();

console.log(Circle);
