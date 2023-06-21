//Getters and Setters 

const person = {
    firstName : 'Mosh',
    lastName : 'Hamedani',
    get fullName() {
        return `${person.firstName} ${person.lastName}`;
},

    set fullName(value) {
        const parts = value.split(' ');
        this.firstName = parts[0];
        this.lastName = parts[1];
    }
};

person.fullName = 'John Smith';
console.log(person);

//Try and Catch

const person = {
    firstName : 'Mosh',
    lastName : 'Hamedani',
    get fullName() {   
        if(typeof value !== 'string')
            throw new Error ('value is not a string.');

        const parts = value.split(' ');
        if(parts.length !== 2)
            throw new Error('Enter a frist and last name:');
            this.firstName = parts[0];
            this.lastName = parts[1];
}
};

try {
    person.fullName = '';
}
catch (e) {
    alert(e);
}

console.log(person);

