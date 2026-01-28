"""
As input data, you have a list of strings.
Write a method double_string() for counting the number of strings from the list, represented in the form
of the concatenation of two strings from this arguments  list.
For example: data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))
Result = 3
"""

def double_string(data):
    counter = 0
    for index, value in enumerate(data):
        for next_i in data[index+1:]:
            if value in next_i:
                counter += 1
                break
    return counter

data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data)) #3

data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data)) #3

data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data)) #4
