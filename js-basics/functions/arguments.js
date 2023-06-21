//Arguments

function sum() {
    let total = 0;
    for(let value of arguments)
        total += value;
    return total;
}

console.log(sum(1,2,3,4,5,10));

// Rest operator

function sum(discount, ...prices) {
    const total = prices.reduce((a,b) => a+b);
    return total *(1-discount);
}

console.log(sum(0.1,20,30,1));

//default parameters

function interest (principal, rate = 3.5, years) {
    return principal *rate /100*years;
}

console.log(interest(10000, undefined, 5));
