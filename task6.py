# UofE ANLP (AY18/19) Assignment 1: Language modelling
"""
TASK6: Intrinsic language evaluation
 - Perplexity is an intrisic measure
 - We can evaluate not the language model on the task - extrinsic
 - Task: word generation:
   - Generate works and measure their preplexity under the LM
   - This is efectively doing task 4 and 5 together
"""
import sys
import random
from math import log
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
Helper function to estimate the perplexity
of the sequence given the model.
INPUT - Language model, sequence
OUTPU - Preplexity
"""
def generate_word_from_LM(model):
    # Initialize word end start pointer to have
    # proper sequence generation
    word = '##'
    # Generate first character
    while True:

        distribution   = get_distribution(model=model, seq=word[-2:])
        char = get_char(distribution = distribution)
        # Check if one of the word stoping characters were not generated
        if char not in ['#', '.', ' ']:
            word = word + char
        # Do not allow one letter sequence (its not supported by this language
        # Model
        elif len(word) == 2:
            word = '##'
        # If finishe generated, finish the sequence
        else:
            word = word + '#'
            return word

# I/O : Provide the name of the language model
if len(sys.argv) != 2:
    print("Wrong number of inputs")
    sys.exit(1)

# Read Language model
LM = {}
with open('model/' + sys.argv[1]) as f:
    for line in f:
        elem = line.split('\t')
        # Removing newline left in parsing
        LM[elem[0]] = elem[1][:-1]

# Generate 100 words with the given language model and calculate their preplexities:

with open('results/words' + sys.argv[1][-6:], 'w+') as f:
    for _ in range(0,101):
        word       = generate_word_from_LM(model=LM)
        f.write(word[2:-1] + '\n')
