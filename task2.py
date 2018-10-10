# UofE ANLP (AY18/19) Assignment 1: Language modelling

"""
TASK2: Infering the language model for model-br.en

Observations:
(1) usage of sequence characters
- fst char : 30 (letters+ 0 + space + . + #)
- snd char : 29 (letters+ 0 + space + .    )
- trd char : 30 (letters+ 0 + space + . + #)
which implies that probability to see any charcter after #
is zero (what is expected as it is end of sequence marker)

(2) We inspect smoothing applied as there is no zero 
probability sequence. 

(3) inintial sequence is inprobable 

"""