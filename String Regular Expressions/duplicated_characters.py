import re
"""
As input data, you have a string that consists of words that have duplicated characters at the end of it.
All duplications may be in the next format:
wordxxxx
wordxyxyxy
wordxyzxyzxyz, where x, xy or xyz repeated ending of the word
Using re module write function pretty_message() that remove all duplications
"""
def pretty_message(str):
    cleaned_data = []
    pattern = r'(.+?)\1+'
    for d in str.split():
        cleaned_data.append(re.sub(pattern,r'\1', d))
    final_data = ' '.join(cleaned_data)
    return final_data

data = "wordxxxx wordxyxyxy wordxyzxyzxyz"
print(pretty_message(data))  #wordx wordxy wordxyz

data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data)) #This is echo string. Replace repeated groups of symbols