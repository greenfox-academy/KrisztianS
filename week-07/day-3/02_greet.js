'use strict';

var al = 'Greenfox'

function greet(inp) {
    if (inp == undefined){
        console.log('Greetings, dear Guest!')
    } else {
    console.log('Greetings, dear ' + inp + '!')
    }
};

greet(al)

// - Create variable named `al` and assign the value `Greenfox` to it
// - Create a function called `greet` that greets it's input parameter
//     - Greeting is printing e.g. `Greetings, dear Greenfox`
//     - Prepare for the special case when no parameters are given
// - Greet `al`