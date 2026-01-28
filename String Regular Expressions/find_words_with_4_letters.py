import re
"""
How would you find a word or words that end in 4 lowercase letters and have at least 
one zero in front of them? Write a regular expression.
For example, in line "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg" this pattern matches 
the words "00000xbcd", "hjkj00wjhg", "hjkj0ajhg"
"""


def pretty_message(str):
    words_end_lower = []
    pattern = r'.?(0+[a-z]{4})\b'
    for w in str.strip('.').split():
        if re.findall(pattern, w):
            words_end_lower.append(w)
    return words_end_lower

print(pretty_message("0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg")) #['00000xbcd', 'hjkj00wjhg', 'hjkj0ajhg']

print(pretty_message("0alpha 0beta 0gamma 0delta")) #['0beta']

