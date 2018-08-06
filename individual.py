import numpy as np
from math import pi
import random as rand

SPECIES_SIZES = {
        'wizard': 1.0,
        'human': 2.0,
        'orc': 3.0
        }
SPECIES_STRYCH_EFFECT = {
        'wizard': 0.0,
        'human': 1.0,
        'orc': 0.5
        }
TRANSLATE_SIZE = 1.0
STRYCH_MAX = 0.4
SIZE_RANDOMIZER = 1.0


class Creature(object):
    def __init__(self, species, mfc=None, strychnine=None):
        self.species = species
        self.strychnine = strychnine or rand.random()*STRYCH_MAX

        d1, d2, d3, d4 = (self._make_x() for n in range(4))
        self.corners = tuple(np.array(x) 
                for x in ((0,d1), (-1*d2,0), (0,-1*d3), (d4, 0))
                )

        self.rotate()
        self.translate()
        return
        

    def _make_x(self):
        size = SPECIES_SIZES[self.species]
        srand = SIZE_RANDOMIZER
        x = size + rand.uniform(-1*srand, srand) - self.strychnine
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
        
