"""
Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string that reads the same left-to-right and right-to-left.
Example
"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
[input] string s (min 1 letters)
[output] boolean
"""

def is_palindrome(str):
    odd_count = 0
    for el in set(str):
        if str.count(el) % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


print(is_palindrome("trueitrue")) #True
print(is_palindrome("trueistrue")) #False
print(is_palindrome("qqqrrrwww")) #False




