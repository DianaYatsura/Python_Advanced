#Create function create_account(user_name: string, password: string, secret_words: list).
#This function should return inner function check.
#The function check compares the values of its arguments with password and secret_words:
#the password must match completely, secret_words may be misspelled (just one element).
#Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,
#special character and one number.
#Otherwise function create_account raises ValueError.
#For example:
#tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error
#If tom = create_account("Tom", "Qwerty1_", ["1", "word"])
#then tom("Qwerty1_",  ["1", "word"]) return True
#tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]
#tom("Qwerty1_",  ["word", "12"]) return True
#tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"

import re


def create_account(user_name: str, password: str, secret_words: list):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{6,}$"
    if not re.match(pattern, password):
        raise ValueError('Password should contain at least 6 symbols including one uppercase letter, '\
                         'one lowercase letter,  special character and one number.')

    saved_password = password
    saved_secret_words = set(secret_words)
    saved_length = len(secret_words)

    def check(password: str, secret_words: list):
        if password != saved_password:
            return False

        if len(secret_words) != saved_length:
            return False

        current_secret_words = set(secret_words)
        common_secret = saved_secret_words.intersection(current_secret_words)
        count = saved_length - len(common_secret)
        return count <=1

    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_",  ["1", "word"])
print(check1) #True

check2 = tom("Qwerty1_",  ["word"])
print(check2) #False

check3 = tom("Qwerty1_",  ["word", "2"])
print(check3) #True

check4 = tom("Qwerty1!",  ["word", "12"])
print(check4) #False

