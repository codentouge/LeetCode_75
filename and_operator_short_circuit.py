
str1 = "noat"
str2 = "with@"


def check_symbol(string, char="@"):
    position = 0
    global contains_char
    contains_char = ""
    '''
    1. while string[position] != char and position < len(string): ==> WRONG
    2. while position < len(string) and string[position] != char: ==> CORRECT

    In Python, the and operator performs short-circuit evaluation, which means that if the first condition is false, the second condition is not evaluated at all. 
    '''
    while position < len(string) and string[position] != char:
        position += 1

    if position >= len(string):
        contains_char = False
    else:
        contains_char = True

check_symbol(str2)
print(contains_char)
