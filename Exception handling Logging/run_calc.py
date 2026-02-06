#We have a function calc(a, b, op). Write your code insode run_calc with calling of function calc.
# Script must work with any arguments. Catch ValueError and print it, catch TypeError and print "TypeError",
# Catch error of division by zero and print "Division by zero". After call calc print "End of calculation"
# in all cases.

def calc(a, b, op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b
    raise ValueError('Incorrect operation is obtained')


def run_calc(a, b, op):
    try:
        result = calc(a, b, op)
        print(result)
    except ValueError as e:
        print(e)
    except TypeError:
        print('TypeError')
    except ZeroDivisionError:
        print("Division by zero")
    finally:
        print("End of calculation")


run_calc(1, 2, 0) #3
                            #End of calculation

run_calc(-19, "String", 3) #TypeError
                                  #End of calculation