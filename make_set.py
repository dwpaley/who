import individual
import pickle
import sys
import random as rand

def rand_who(nw, nh, no): 
    return rand.sample((nw*['w'] + nh*['h'] + no*['o']), 1)[0]

def rand_mfc(nm, nf, nc): 
    return rand.sample((nm*['m'] + nf*['f'] + nc*['c']), 1)[0]

with open(sys.argv[1], 'wb') as f:
    out_list = [
            individual.Creature(rand_who(1,1,1), rand_mfc(1,1,1))
            for n in range(100)
            ]
    pickle.dump(out_list, f)
