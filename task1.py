# UofE ANLP (AY18/19) Assignment 1: Language modelling
"""
TASK1: Writing function preprocess_line to remove 
Unwanted character from the description.

We extend the abilities of this function by considering
the extended problem of introducting doulbe space after 
the character removal. 

INPUT  - String
OUTPUT - String
"""
def preprocess_line(line):
    newline = ['#'] # include sequence begining marker
    upper = [chr(i) for i in range(65, 91)]  # [A-Z]
    lower = [chr(i) for i in range(97, 123)] # [a-z]
    special = [' ', '.']                    
    digits = [chr(i)for i in range(48, 58)]  # [0-9]
    previous_char = "" # marker for double space problem
    for character in line:
        if character in upper:
            newline.append(character.lower())
            previous_char = character
        if character in lower:
            newline.append(character)
            previous_char = character
        if character in special and previous_char != ' ':
            newline.append(character)
            previous_char = character
        if character in digits:
            newline.append('0')
            previous_char = character
    newline.append('#') # Include sequence end marker
    return "".join(newline)