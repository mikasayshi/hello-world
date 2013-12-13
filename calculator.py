#! /usr/bin/env python

def square(x):
    return x * x

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


#a = input("plz gimme 1st numba: ")
#b = input("plz gimme 2nd numba: ")
#print multiply(a, b)


words = ["mika", "says", "hi", "again", "and", "again"]
print len(words)

for index in range(0, len(words)): # [0, 1, 2]
    print words[index]
