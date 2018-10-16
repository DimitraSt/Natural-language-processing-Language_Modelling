# UofE ANLP (AY18/19) Assignment 1: Language modelling

"""
TASK2: Infering the language model for model-br.en
"""

import numpy as np 

# Solving matrix equation
# Mx = b

## 	1.021e-05
##.	1.021e-05
##0	1.021e-05
##a	6.730e-02
##b	2.758e-02
##c	3.983e-02
##d	4.259e-02
##e	2.359e-03
##f	9.303e-03
##g	1.808e-02
##h	6.536e-02
##i	8.313e-02
##j	5.627e-03
##k	1.083e-02
##l	5.066e-02
##m	1.696e-02
##n	3.401e-02
##o	4.555e-02
##p	2.881e-02
##q	9.292e-04
##r	9.405e-03
##s	4.004e-02
##t	1.194e-01
##u	1.746e-03
##v	1.236e-03
##w	1.795e-01
##x	2.144e-04
##y	9.865e-02
##z	8.271e-04

M = np.matrix(
    [
        [1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,
         1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,
         1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05, 1.021e-05*30-1],
        [1.021e-05-1,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,
        1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,
        1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05, 1.021e-05*30-1],
        [1.021e-05,1.021e-05-1,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,
        1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,
        1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05,1.021e-05*30-1],
        [6.730e-02,6.730e-02,6.730e-02-1,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,
        6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,
        6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02,6.730e-02*30-1],
        [2.758e-02,2.758e-02,2.758e-02,2.758e-02-1,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,
        2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,
        2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02,2.758e-02*30-1],
        [3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02-1,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,
        3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,
        3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02,3.983e-02*30-1],
        [4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02-1,4.259e-02,4.259e-02,4.259e-02,4.259e-02,
        4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,
        4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02,4.259e-02*30-1],
        [2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03-1,2.359e-03,2.359e-03,2.359e-03,
        2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,
        2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03,2.359e-03*30-1],
        [9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03-1,9.303e-03,9.303e-03,
        9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,
        9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03,9.303e-03*30-1],
        [1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02-1,1.808e-02,
        1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,
        1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02,1.808e-02*30-1,],
        [6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02-1,
        6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,
        6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02,6.536e-02*30-1],
        [8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,
        8.313e-02-1,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,
        8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02,8.313e-02*30-1],
        [5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,
        5.627e-03,5.627e-03-1,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,
        5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03,5.627e-03*30-1],
        [1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,
        1.083e-02,1.083e-02,1.083e-02-1,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,
        1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02,1.083e-02*30-1],
        [5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,
        5.066e-02,5.066e-02,5.066e-02,5.066e-02-1,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,
        5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02,5.066e-02*30-1],
        [1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-0,1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02,
        1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02-1,1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02, 
        1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02,1.696e-02*30-1],
        [3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,
        3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02-1,3.401e-02,3.401e-02,3.401e-02,3.401e-02,
        3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02,3.401e-02*30-1],
        [4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,
        4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02-1,4.555e-02,4.555e-02,4.555e-02,
        4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02,4.555e-02*30-1],
        [2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,
        2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02-1,2.881e-02,2.881e-02,
        2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02,2.881e-02*30-1],
        [9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,
        9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04-1,9.292e-04,
        9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04,9.292e-04*30-1],
        [9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,
        9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03-1,
        9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03,9.405e-03*30-1],
        [4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,
        4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,
        4.004e-02-1,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02,4.004e-02*30-1],
        [1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,
        1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,
        1.194e-01,1.194e-01-1,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01,1.194e-01*30-1],
        [1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,
        1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,
        1.746e-03,1.746e-03,1.746e-03-1,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03,1.746e-03*30-1],
        [1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,
        1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,
        1.236e-03,1.236e-03,1.236e-03,1.236e-03-1,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03,1.236e-03*30-1],
        [1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,
        1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01,
        1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01-1,1.795e-01,1.795e-01,1.795e-01,1.795e-01,1.795e-01*30-1],
        [2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,
        2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,
        2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04,2.144e-04-1,2.144e-04,2.144e-04,2.144e-04,2.144e-04*30-1],
        [9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,
        9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,
        9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02,9.865e-02-1,9.865e-02,9.865e-02,9.865e-02*30-1],
        [8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,
        8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,
        8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04,8.271e-04-1,8.271e-04,8.271e-04*30-1]
    

        
    
)

# Finish with 10