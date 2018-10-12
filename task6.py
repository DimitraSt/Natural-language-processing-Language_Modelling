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
from task5 import preplexity_seq
from task4 import get_char, get_distribution

def generate_word_from_LM(model):
    # Initialize word end start pointer to have
    # proper sequence generation
    word = '##'
    # Generate sequence
    while True:

        distribution   = get_distribution(model=model, seq=word)
        char = get_char(distribution = distribution)
        # Check if one of the word stoping characters were not generated
        if char != ('#' or '.' or ' '):
            word = word + char
        # If generated, finish the sequence instead
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

with open('results/gen-perplexity' + sys.argv[1][-6:], 'w+') as f:
    for _ in range(0,101):
        word       = generate_word_from_LM(model=LM)
        perplexity = preplexity_seq(model=LM, seq=word)
        f.write(word + '\t' + perplexity)
