'use strict'

const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
        this.cash += amt
    }
}

const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
        this.cash += amt
    }
}

const Shuffler = {
    cash: 10000,
    counter: 0,
    pick: function() {
        this.cash -= 1000;
        if (this.counter % 2 === 0) {
            Panama.cash += 1000;
            this.counter +=1
            console.log('Panama got 1000')
        } else {
            Cyprus.cash += 1000;
            this.counter += 1;
            console.log('Cyprus got 1000')
            }

        }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 