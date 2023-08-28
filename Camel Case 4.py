import re
import sys

def main_loop(arg):
    operation, token, *words = arg
    words = " ".join(words)

    if operation == "C":
        output = combiner(words, token)
    elif operation == "S":
        output = splitter(words, token)
    
    print(output)
        
def splitter(words, token):
    output = []

    if token == "C":
        words = re.sub(r'([a-z])([A-Z])', r'\1 \2', words)
        output = words.lower()
    
    elif token == "V":
        words = re.sub(r'([a-z])([A-Z])', r'\1 \2', words)
        output = words.lower()
    
    elif token == "M":
        words = words[:-2]
        words = re.sub(r'([a-z])([A-Z])', r'\1 \2', words)
        output = words.lower()

    return output

def combiner(words, token):
    output = ""

    if token == "C":
        capitalized = words.title()
        output = "".join(capitalized.split())

    elif token == "V":
        words_list = words.split()
        modified_words = [words_list[0]] + [word.capitalize() for word in words_list[1:]]
        output = "".join(modified_words)

    elif token == "M":
        words_list = words.split()
        modified_words = [words_list[0]] + [word.capitalize() for word in words_list[1:]]
        output = "".join(modified_words) + "()"

    return output

for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespace, including newline characters
    if not line:
        continue  # Skip empty lines
    main_loop(line.split(";"))

