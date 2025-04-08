import math, queue
from collections import Counter
#from test_main import *

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    elif S[0] == T[0]:
        return MED(S[1:], T[1:])
    else:
        insert = MED(S, T[1:])
        delete = MED(S[1:], T)
        substitute = MED(S[1:], T[1:])
        return 1 + min(insert, delete, substitute)



def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    key = (S, T)
    if key in MED:
        return MED[key]
    
    if S == "":
        MED[key] = len(T)
    elif T == "":
        MED[key] = len(S)
    elif S[0] == T[0]:
        MED[key] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        substitute = fast_MED(S[1:], T[1:], MED)
        MED[key] = 1 + min(insert, delete, substitute)

    return MED[key]
    pass

def fast_align_MED(S, T, MED=None):
    if MED is None:
        MED = {}
        
    key = (S, T)
    if key in MED:
        return MED[key]
    
    if S == "":
        MED[key] = ('-' * len(T), T)
    elif T == "":
        MED[key] = (S, '-' * len(S))
    elif S[0] == T[0]:
        align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        MED[key] = (S[0] + align_S, T[0] + align_T)
    else:
        # Try insert
        insert_S, insert_T = fast_align_MED(S, T[1:], MED)
        insert = (1 + fast_MED(S, T[1:]), '-' + insert_S, T[0] + insert_T)

        # Try delete
        delete_S, delete_T = fast_align_MED(S[1:], T, MED)
        delete = (1 + fast_MED(S[1:], T), S[0] + delete_S, '-' + delete_T)

        # Try substitute
        sub_S, sub_T = fast_align_MED(S[1:], T[1:], MED)
        sub = (1 + fast_MED(S[1:], T[1:]), S[0] + sub_S, T[0] + sub_T)

        # Choose the option with the smallest cost
        best = min([insert, delete, sub], key=lambda x: x[0])
        MED[key] = (best[1], best[2])

    return MED[key]

    pass

