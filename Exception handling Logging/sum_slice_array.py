#Write the function sum_slice_array(arr, first, second), which accepts the array (list) arr and
# two numbers (first and second) - the ordinal numbers of the elements of the array that must be added.
# For example, if 3 and 5 were entered, the 3rd and 5th elements must be added.
#The function should generate exceptions MyExceptions:
#if non-numbers or numbers less than 1 were entered;
#if non-numbers obtained from array;
#if when one of the numbers or both is larger than the array length.

class MyExceptions(Exception):
    def __init__(self):
        super().__init__()

def sum_slice_array(arr, first, second):
    if not (isinstance(first, int) and isinstance(second, int)):
        raise MyExceptions
    if first < 1 or second < 1:
        raise MyExceptions
    if first > len(arr) or second > len(arr):
        raise MyExceptions
    el1 = arr[first - 1]
    el2 = arr[second - 1]
    if not (isinstance(el1, (float, int)) and isinstance(el2, (float, int))):
        raise MyExceptions
    return float(el1 + el2)



print(sum_slice_array([1, 2, 3], 1, 2)) #3.0

try:
    print(sum_slice_array([1, "string", 3], 1, 2))
except MyExceptions:
    print("MyExceptions") #MyExceptions

try:
    print(sum_slice_array([14, 5, 3], -1, 2))
except MyExceptions:
    print("MyExceptions") #MyExceptions
