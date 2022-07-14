// TODO: Add import statement

class Person {
    name: string; //TODO: update the name field to something else
    age: number;
}

// createPerson call is a factory method

function createPerson() : Person {
    return {
        name: "A Person",// A Person's name
        age: 33 /// TOdo: Should be parsed with triple forward slash 
    }
}

// todo: lowercase todo comment should also be parsed

//TODO: Uppercase, right after two forward slash, should be parsed
//todo: Lowercase, right after two forward slash, should be parsed
////TODo: Should be parsed regardless of number of forward slash
////todo: Should be parsed regardless of number of forward slash

// This file should parse 8 to-dos