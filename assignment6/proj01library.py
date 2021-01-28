"""
Name: Peter Mark Kaiganaine
Reg No: F21/136578/2019
"""


ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"
# Added
ALPHA_NUMERICS = ASCII_LOWERCASE + ASCII_UPPERCASE


def is_alpha(string: str):
    for letters in string:
        if letters not in ALPHA_NUMERICS:
            return False
    return True


def is_digit(string: str):
    for letters in string:
        if letters not in DECIMAL_DIGITS:
            return False
    return True


def to_lower(string: str):
    for letters in string:
        if letters not in ASCII_LOWERCASE:
            return string.lower()
    return string


def to_upper(string: str):
    for letters in string:
        if letters not in ASCII_UPPERCASE:
            return string.upper()
    return string


def find_chr(string1: str, string2: str):
    if len(string2) == 1:
        if string2 in string1:
            return string1.index(string2)
    return -1


def find_str(string1: str, string2: str):
    if string2 in string1:
        return string1.index(string2)
    return -1


def replace_chr(string1: str, string2: str, string3: str):
    if len(string2) == 1 and len(string3) == 1:
        if string2 in string1:
            return string1.replace(string2, string3)
    return " "


def replace_str(string1: str, string2: str, string3: str):
    if string2 in string1:
        return string1.replace(string2, string3)
    elif len(string2.strip()) == 0:
        return f'{string3}{string3.join(string1[i:i + 1] for i in range(0, len(string1), 1))}{string3}'
    elif string2 not in string1:
        return string1
