//if - else statement

let hour = 19;

if(hour>=6 && hour<=12){
    console.log("Good Morning")
}
else if(hour>=12 && hour<=18){
    console.log("Good Afternoon")
}else{
    console.log("Good Evening")
}

//switch - case statement

let role = "Guest";

switch(role){
    case "Guest":
        console.log("Guest user")
        break;

    case "Moderate":
        console.log("Moderate user")
        break;

    default:
        console.log("Unkown user")
}