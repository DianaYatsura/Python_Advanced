"""
Numbers in the Morse code have the following pattern:
all digits consist of 5 characters;
the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
starting with the number 6, each dot is replaced by a dash and vise versa.
Write the function morse_number() for encryption of a number in a three-digit format in Morse code.
For example:
print(morse_number("295")) # ..--- ----. .....
print(morse_number("005")) # ----- ----- .....
"""
def  morse_number(str):
    parts = []
    for n in str:
        digit = int(n)
        if digit in range(1, 6):
            morse = ('.' * digit).ljust(5, '-')
            parts.append(morse)
        elif digit in range(6, 10):
            morse = ('-' * (digit-5)).ljust(5, '.')
            parts.append(morse)
        else:
            morse = ('-' * 5).ljust(5)
            parts.append(morse)
    result=" ".join(parts)
    return result

print(morse_number('295')) #..--- ----. .....
print(morse_number("005")) #----- ----- .....
print(morse_number("513")) #..... .---- ...--
