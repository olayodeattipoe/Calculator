def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}

function = operations['*']
print(type(function))
answer = function(2, 4)
print(answer)