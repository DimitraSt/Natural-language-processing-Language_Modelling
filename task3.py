# UofE ANLP (AY18/19) Assignment 1: Language modelling
"""
TASK3: Estimating Language model from the given file
- Implement +alpha smoothing method
N = 30 (26 letters + # + . + space)
"""
from task1 import preprocess_line
import sys
from collections import defaultdict
from math import log2


# Template for language model
def get_template():
    all_tri ={}
    with open('model/model-br.en', 'r') as f:
        for line in f:
            # Take the first value in template
            tri = line.split('\t')[0]
            all_tri[tri] = 0
    return all_tri
    
def estimate_distribution(counts, alpha=1):
    probs = {}
    total = sum(list(counts.values()))

    for tri in counts.keys():
        probs[tri] = (counts[tri] + alpha)/( total + 30*alpha)

    return probs 

def preplexity_seq(model, seq):

    cross_entropy = 0
    # '#' + seq := hack to have proper conditioning
    for i in range(len('#' + seq)-(3)):
        tri = seq[i:i+3]
        cross_entropy += log2(float(model[tri]))
    cross_entropy = -1 / len(seq) * cross_entropy

    return 2**cross_entropy

def estimate_preplexity(model, data):

    total_perplexity=0 
    num = 0
    for line in data:
        preplexity = preplexity_seq(model = model, seq = line)
        total_perplexity += preplexity
        num += 1
    avg_perplexity = total_perplexity / num

    return avg_perplexity

def estimate_model(tri_counts, alpha=1):

    model = get_template()
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
            model.update(prob)
            common_two = {tri: tri_counts[tri]}


    # Extra for last common_two
    prob = estimate_distribution(counts=common_two,alpha=alpha)
    model.update(prob)

    return model

def final_model(path, alpha=1):
    
    tri_counts = get_template()
    with open('data/' + path) as f:
        for line in f:
            line = preprocess_line(line)
            for j in range(len(line)-(3)):
                    tri = line[j:j+3]
                    tri_counts[tri] = tri_counts[tri] + 1
        
        model = estimate_model(tri_counts=tri_counts, alpha=alpha)

    return model


def validate_model(path, alpha=1, k=5):

    folds = []
    fold  = []
    file_size = len(open('data/' + path).readlines())
    with open('data/' + path) as f:
        for line in f:
            line = preprocess_line(line)
            # Single char per line problem
            fold.append(line)
            # check if you finished the fold
            if len(fold) == file_size/k:
                # add fold to folds
                folds.append(fold)
                fold = []
        # Extra processing for the last fold 
        # if it is not divisible by k
        folds.append(fold)

    ## Prepexity list
    pps = []
    # k folds processing
    for i in range(k):

        train    = folds[:i] + folds[i+1:]
        validate = folds[i]
        
        # create count template 
        tri_counts = get_template()

        # estimate counts
        for elem in train:
            for j in range(len(line)-(3)):
                tri = line[j:j+3]
                tri_counts[tri] = tri_counts[tri] + 1
        
        # estimate model
        LM = estimate_model(tri_counts=tri_counts, alpha=alpha)

        # evaluate model
        pp = estimate_preplexity(model=LM, data=validate)
        pps.append(pp)

        print("model alpha = " + str(alpha) + " fold: " + str(i+1) + " pp: " + str(pp))

    avg_pp = sum(pps)/len(pps)

    return LM, avg_pp

"""
MAIN PROGRAM 
"""   

# I/O : Provide the name of the training file
if len(sys.argv) != 2:
    print("Wrong number of arguments")
    sys.exit(1)

infile = sys.argv[1] 

# define possible alpha values to test
alphas = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]

best_model, best_pp = validate_model(path=infile, alpha=0.1)
best_alpha = 0.1

for alpha in alphas:

    model, pp = validate_model(path=infile, alpha=alpha)
    print("model alpha = " + str(alpha) + "pp: " + str(pp))

    if pp < best_pp:
        best_pp = pp
        best_alpha = alpha

print("===================================================")
print("The best model alpha = " + str(best_alpha) + " with pp: " + str(best_pp))

# Train the model with best alpha and all data:
model = final_model(path=infile, alpha = best_alpha)

# STEP 3: Save estimate to the file
with open('model/model-my.'+infile[-2:], 'w+') as f:
    for tri in sorted(model.keys()):
        f.write(tri + '\t ' + str(model[tri]) + '\n')