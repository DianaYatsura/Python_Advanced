"""
Convert a certain expression like 2+3 to expression in a postfix notation.
The given expression can have one of the following tokens:
a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
devision (/);
modulo operation (%).
Example:
For expression = ["2","+","3"] the output should be ["2","3","+"].
[execution time limit] 4 seconds (py)
[input] array.string expression
An array of tokens of a valid expression in the standard notation.
[output] array.string
Tokens of the expression in the postfix notation.
"""


def toPostFixExpression(e):
    postfix = []
    stack = []
    priority = {
                '+': 1,
                '-': 1,
                '*': 2,
                '/': 2
                }
    for el in e:
        if el.isdigit():
            postfix.append(el)
        elif el in priority:
            while (stack and stack[-1] in priority and
                   priority[stack[-1]] >= priority[el]):
                postfix.append(stack.pop())
            stack.append(el)
        elif el == '(':
            stack.append(el)
        elif el == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

    while stack:
        postfix.append(stack.pop())

    return postfix


print(toPostFixExpression(e = ["2","+","3"])) #['2', '3', '+']
print(toPostFixExpression(["20",
                           "+",
                           "3",
                           "*",
                           "(",
                           "5",
                           "*",
                           "4",
                           ")"])) #['20', '3', '5', '4', '*', '*', '+']