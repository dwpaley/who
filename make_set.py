import individual
import pickle
import sys
import random as rand
import matplotlib.pyplot as plt

WHO_ODDS = (1,1,1)
MFC_ODDS = (1,1,1)

def rand_who(nw, nh, no): 
    return rand.sample((nw*['w'] + nh*['h'] + no*['o']), 1)[0]

def rand_mfc(nm, nf, nc): 
    return rand.sample((nm*['m'] + nf*['f'] + nc*['c']), 1)[0]


def make_creature_list(n):

    out = [
            individual.Creature(rand_who(*WHO_ODDS), rand_mfc(*MFC_ODDS))
            for i in range(n)
            ]
    return out



if __name__ == '__main__':
    with open(sys.argv[2], 'wb') as f:
        pickle.dump(make_creature_list(int(sys.argv[1])), f)
