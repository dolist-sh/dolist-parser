// TODO: This should be parsed

class Person {
    name: string;
    age: number;
}

// This should not be parsed, as it's not TODO comment

function createPerson() : Person {
    return {
        name: "Yunjae",
        age: 33 // todo: THIS SHOULD ALSO BE PARSED
    } /**
    this is not a todo comment
    */
}

/**
 * 
 * TODO: this is a todo comment
 */

/**
 * 
TODO comment */


/**
 * 
 * 
 * This is not a todo comment
 */

// todo: this should also be parsed

//TODO: This should be parsed
//todo: This should be parsed
