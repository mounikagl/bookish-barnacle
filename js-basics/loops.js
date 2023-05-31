// for loops

for(i=0; i<=5; i++){
    console.log("Hello");
    console.log(i);
}

for(i=0; i<=5; i++){
    if(i%2!==0){
        console.log(i);
    }
}

// while loops

let i=0;

while(i<=5){
    if(i%2!==0){
        console.log(i)
    }
    i++;
}

// Do - while loops

let i = 0;
do{
    if(i%2 !==0)
    console.log(i);
    i++;
}while(i<5)

// for - in 

const person = {
    name : "Mosh",
    age : 30,
};

for (let key in person){
    console.log(key, person[key]);
}


// for - of 

const colors = ['red', 'green', 'blue'];

for (color of colors){
    console.log(color);
}



// Break and Continue

let i = 0;

while(i<=10){
    if(i === 5)
    break;

    console.log(i);
    i++;
}

