# UofE ANLP (AY18/19) Assignment 1: Language modelling
"""
TASK3: Estimating Language model from the given file
- Implement +1 smoothing method
N = 30 (26 letters + # + . + space)
"""
from task1 import preprocess_line
import sys
from collections import defaultdict

def estimate_distribution(counts, alpha=1):
    probs = {}
    total = sum(list(counts.values()))

    for tri in counts.keys():
        probs[tri] = (counts[tri] + alpha)/( total + 30*alpha)

    return probs 

tri_counts = defaultdict(int)
tri_prob   = {}

# I/O : Provide the name of the training file
if len(sys.argv) != 3:
    print("Wrong number of arguments")
    sys.exit(1)

infile = sys.argv[1] 
alpha  = float(sys.argv[2])

# STEP 1: Read the file and obtain the count of triples
with open('data/' + infile) as f:
    for line in f:
        line = preprocess_line(line)
        for j in range(len(line)-(3)):
            tri = line[j:j+3]
            tri_counts[tri] = tri_counts[tri] + 1

# STEP 2: Extimate probabilities

# obtain all sequences sequence in the given
# model-br.en file (using it as template)
all_tri =[]
with open('model/model-br.en', 'r') as f:
    for line in f:
        # Take the first value in template
        tri = line.split('\t')[0]
        all_tri.append(tri)

# Change tri_count to to suit template format
# by adding value 0 to all the keys unobserved
for tri in all_tri:

    if tri not in list(tri_counts.keys()):
        tri_counts[tri] = 0

# Used to agregate all first two char sequences
common_two = {}
# Do trough all the triples
for tri in sorted(tri_counts.keys()):

    # Check if dict is emply or contains key with the same
    # common two. If so add tri to common_two
    two_so_far = [tr[:2] for tr in list(common_two.keys())]
    if not common_two or tri[:2] in two_so_far:
        common_two[tri] = tri_counts[tri]
    # Else: obtained all counts for distribution
    # Can estimate and clean common_two
    else:
        prob = estimate_distribution(counts=common_two, alpha=alpha)
        tri_prob.update(prob)
        common_two = {tri: tri_counts[tri]}

# Extra for last common_two
prob = estimate_distribution(counts=common_two,alpha=alpha)
tri_prob.update(prob)

# STEP 3: Save estimate to the file
with open('model/model-my.'+infile[-2:], 'w+') as f:
    for tri in sorted(tri_prob.keys()):
        f.write(tri + '\t ' + str(tri_prob[tri]) + '\n')

