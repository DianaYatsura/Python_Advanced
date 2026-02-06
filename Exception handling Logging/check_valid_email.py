import re

def valid_email(email):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
    try:
        if re.fullmatch(pattern, email):
            return "Email is valid"
        else:
            return "Email is not valid"
    except TypeError as te:
        return te

print(valid_email("trafik@ukr.tel.com")) #Email is valid
print(valid_email("trafik@ukr_tel.com")) #Email is not valid
print(valid_email("ownsite@our.c0m")) #Email is not valid
print(valid_email("tra@fik@ukr.com")) #Email is not valid