# UofE ANLP (AY18/19) Assignment 1: Language modelling
"""
TASK6: language generation using value iteration
"""

def get_LM(path):

    LM = {}
    with open('model/' + path) as f:
        for line in f:
            elem = line.split('\t')
            # Removing newtheline left in parsing
            LM[elem[0]] = elem[1][:-1]
    return LM


"""
Arguments:
States: N (number of characters to generate)
Actions: choose one of V=30 char
Reward: 1/perplexity under the current total sequence 
Transition: Language model 

theta: thershold when to stop
"""
def value_iteration()
    
  
