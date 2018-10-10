# UofE ANLP (AY18/19) Assignment 1: Language modelling
"""
TASK1: Estimate preplexity under the given 
language model
"""
import sys
from math import log
from task1 import preprocess_line
"""
Helper function to estimate the perplexity
of the sequence given the model.
INPUT - Language model, sequence
OUTPU - Preplexity
"""
def preplexity_seq(model, seq):

    cross_entropy = 0
    # '#' + seq := hack to have proper conditioning
    for i in range(len('#' + seq)-(3)):
        tri = seq[i:i+3]
        cross_entropy += log(float(model[tri]))
    cross_entropy = -1/ len(seq) * cross_entropy

    return 2**cross_entropy

def estimate_preplexity(path_to_data, path_to_model):

    total_perplexity=0 

    LM = {}
    with open('model/' + path_to_model) as f:
        for line in f:
            elem = line.split('\t')
            # Removing newline left in parsing
            LM[elem[0]] = elem[1][:-1] 

    with open('data/' + path_to_data) as f:
        for line in f:
            line = preprocess_line(line)
            preplexity = preplexity_seq(model = LM, seq = line)
            total_perplexity += preplexity

    return total_perplexity

# I/O : Provide the name of the language model
if len(sys.argv) != 3:
    print("Wrong number of input")
    sys.exit(1)

test_perplexity = estimate_preplexity(path_to_data=sys.argv[1], path_to_model=sys.argv[2])

with open('results/perplexity' + sys.argv[2][-6:], 'w+') as f:
    f.write(str(test_perplexity))

