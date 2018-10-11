# UofE ANLP (AY18/19) Assignment 1: Language modelling
"""
TASK4: Generate string given the language model
"""
import sys
import random
from collections import defaultdict
"""
Helper function to get distribution given the previous
character set
INPUT  - language model (dictionary),  sequence (2 char)
OUTPUT - distribution given sequence
"""
def get_distribution(model, seq):
    distribution = {}
    for ngram in model.keys():
        if ngram[:2] == seq:
            distribution[ngram] = model[ngram]
    return distribution
"""
Helper function to select the character given 
the distribution of the charcters.
inspired by:
INPUT  - distribution
OUTPUT - character
"""
def get_char(distribution):
    tri = random.choices(
            population=list(distribution.keys()),
            weights=[float(v) for v in list(distribution.values())])
    return tri[0][-1:]
"""
INPUT:  path to language model
OUTPUT: generated String over the language model
"""
def generate_from_LM(path, num_char=300):
    
    # STEP 1: read the language model and store it in dictonary
    LM = {}
    with open('model/' + path) as f:
        for line in f:
            elem = line.split('\t')
            # Removing newline left in parsing
            LM[elem[0]] = elem[1][:-1] 
    
    # Initial simbol for sequence
    sequence = '#' 

    for i in range(num_char):
        # init generation by selecting P(*|##) distribution
        if i == 0: 
            distribution = get_distribution(model=LM, seq='##')
        else:
            distribution = get_distribution(model=LM, seq=sequence[-2:])

        new_char = get_char(distribution)
        # Prevent early termination by resampling (#) and (.)
        while new_char == '#' or new_char == '.':
            new_char = get_char(distribution)
        sequence = sequence + new_char
    
    # Add end of the sequence marker
    sequence = sequence + '#'

    return(sequence)


# I/O : Provide the name of the language model
if len(sys.argv) != 2:
    print('Wrong number of arguments')
    sys.exit(1)

sequence =generate_from_LM(path=sys.argv[1])

with open('results/generate' + sys.argv[1][-6:], 'w+') as f:
    f.write(sequence)
