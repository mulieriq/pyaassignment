"""
Name: Peter Mark Kaiganaine
Reg No: F21/136578/2019
"""

from proj01library import *

if __name__ == '__main__':
    # To Lower
    print('TO LOWER TEST')
    print(f'Test To Lower Case : (Python) to LowerCase ? {to_lower("Python")}')
    # To Upper
    print('TO UPPER TEST')
    print(f'Test To Upper Case : (pythOon) to Upper Case ? {to_upper("pythOon")}')
    # Is Digit Test
    print('IS DIGIT TEST')
    print(f'Test s Digit : (pyt3hon) is in Upper Case ? {is_digit("pyt3hon")}')
    print(f'Test s Digit : (python) is in Upper Case ? {is_digit("python")}')
    print(f'Test s Digit : (12345) is in Upper Case ? {is_digit("12345")}')
    # Is Alpha Test
    print('IS ALPHA TEST')
    print(f'Test is Alpha : (pyt3hon) is alpha ? {is_alpha("pyt3hon")}')
    print(f'Test is Alpha : (pythonLang) is alpha ? {is_alpha("pythonLang")}')
    print(f'Test is Alpha : (Pythonlang) is alpha ? {is_alpha("Pythonlang")}')

    # Find Char Test
    print('Find Char TEST')
    print(f'Test Find Char Index : n in (pyt3hon)? {find_chr("pyt3hon", "n")}')
    print(f'Test Find Char Index : ns in (pyt3hon) ? {find_chr("pyt3hon", "ns")}')
    print(f'Test Find Char Index :  in (pyt3hon) ? {find_chr("pyt3hon", "")}')
    print(f'Test Find Char Index : r in (pyt3hon) ? {find_chr("pyt3hon", "r")}')

    # Find Str Test
    print('Find Char TEST')
    print(f'Test Find Str Index : n in (pyt3hon)? {find_str("pyt3hon lang", "lang")}')
    print(f'Test Find Str Index : ns in (pyt3hon) ? {find_str("pyt3hon", "ns")}')
    print(f'Test Find Str Index : r in (pyt3hon) ? {find_str("pyt3hon", "r")}')

    # Replace Char Test
    print('Replace Char TEST')
    print(f'Replace Char : 3 with 2 in (pyt3hon)? {replace_chr("pyt3hon", "3", "2")}')
    print(f'Replace Char : ns in (pyt3hon) ? {replace_chr("pyt3hon", "ns","df")}')

    # Replace Str Test
    print('Replace Str TEST')
    print(f'Replace Str : lang with lugha in (pyt3hon)? {replace_str("pyt3hon", "3", "2")}')
    print(f'Replace Str : ns in (pyt3hon) ? {replace_str("pyt3hon", "ns","df")}')
    print(f'Replace Str : " "  in (pyt3hon) ? {replace_str("pyt3hon", " ", "df")}')

