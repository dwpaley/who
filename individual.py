import numpy as np
from math import pi
import random as rand

SPECIES_SIZES = {
        'w': {
            'm':     1.5,
            'f':   1.0,
            'c':    0.5
            },
        'h': {
            'm':     2.5,
            'f':   2.0,
            'c':    1.5
            },
        'o': {
            'm':     3.5,
            'f':   3.0,
            'c':    2.5
            }
        }
SPECIES_LEAD_EFFECT = {
        'w': 0.0,
        'h': 1.0,
        'o': 0.5
        }
TRANSLATE_SIZE = 1.0
LEAD_MAX = 0.4
SIZE_RANDOMIZER = 1.0


class Creature(object):
    def __init__(self, species=None, mfc=None, lead=None):
        self.species = species or rand.sample(['w', 'h', 'o'], 1)[0]
        self.mfc = mfc or rand.sample(['m', 'f', 'c'], 1)[0]
        self.lead = lead or rand.random()*LEAD_MAX

        d1, d2, d3, d4 = (self._make_x() for n in range(4))
        self.corners = tuple(np.array(x) 
                for x in ((0,d1), (-1*d2,0), (0,-1*d3), (d4, 0))
                )

        self.rotate()
        self.translate()
        return
        

    def _make_x(self):
        size = SPECIES_SIZES[self.species][self.mfc]
        srand = SIZE_RANDOMIZER
        x = size + rand.uniform(-1*srand, srand) - self.lead
        return x

    def rotate(self, angle=None):
        if not angle: angle=2*pi*rand.random()
        c, s = np.cos(angle), np.sin(angle)
        rot_mat = np.array([[c, -s], [s, c]])
        self.corners = tuple(np.dot(rot_mat, x) for x in self.corners)

    def translate(self, shift=None):
        if not shift: shift = TRANSLATE_SIZE * np.array(
                [rand.random(), rand.random()])
        self.corners = tuple(x + shift for x in self.corners)
        

