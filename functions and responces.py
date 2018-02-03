#!/usr/bin/env python

messages = {"good": "Hi Nasser, boo",
            "bad" : "you are not alowed to see the secret message"
}


def greet(name):
        if name == "nasser":
                print messages["good"]
        else:
                print "Hello " + name
                print messages["bad"]
        



while True:
        name = raw_input("What is your name? ")
        if name != "": break
        
greet(name.lower())


