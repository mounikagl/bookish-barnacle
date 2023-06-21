// const marks = [80, 67, 87];

// console.log(calculateGrade(marks));

// function calculateGrade(marks){
//     let sum =0;
//     for (let mark of marks)
//         sum += mark;
//     let average = sum/marks.length;

//     if (average < 60) return 'F';
//     if (average < 70) return 'D';
//     if (average < 80) return 'C';
//     if (average < 90) return 'B';
//     return 'F';

// }


const array = [80, 67, 87];

console.log(calculateGrade(array));

function calculateAverage(array){
    let sum =0;
    for (let value of array)
        sum += value;
    return sum/array.length;
}

function calculateGrade(array){
    const average = calculateAverage(array);
    if (average < 60) return 'F';
    if (average < 70) return 'D';
    if (average < 80) return 'C';
    if (average < 90) return 'B';
    return 'F';
}