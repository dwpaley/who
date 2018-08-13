import numpy as np
from math import pi
import random as rand
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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

PLOT_COLORS = {
        ('w', 'm'): 'xkcd:red',
        ('w', 'f'): 'xkcd:magenta',
        ('w', 'c'): 'xkcd:lavender',
        ('h', 'm'): 'xkcd:green',
        ('h', 'f'): 'xkcd:light green',
        ('h', 'c'): 'xkcd:mint',
        ('o', 'm'): 'xkcd:navy blue',
        ('o', 'f'): 'xkcd:blue',
        ('o', 'c'): 'xkcd:light blue'
        }




SPECIES_LEAD_EFFECT = {
        'w': 0.0,
        'h': 2.0,
        'o': 1.0
        }
TRANSLATE_SIZE = 3.0
LEAD_MAX = 0.4
SIZE_RANDOMIZER = 0.2


class Creature(object):
    def __init__(self, species=None, mfc=None, lead=None):
        self.species = species or rand.sample(['w', 'h', 'o'], 1)[0]
        self.mfc = mfc or rand.sample(['m', 'f', 'c'], 1)[0]
        self.lead = lead or rand.random()*LEAD_MAX
        self.plot_color = PLOT_COLORS[(self.species, self.mfc)]

        d1, d2, d3, d4 = (self._make_x() for n in range(4))
        self.corners = np.vstack(np.array(x) 
                for x in ((0,d1), (-1*d2,0), (0,-1*d3), (d4, 0))
                )

        self.rotate()
        self.translate()
        self.make_polygon()
        return
        

    def _make_x(self):
        size = SPECIES_SIZES[self.species][self.mfc]
        srand = SIZE_RANDOMIZER
        x = (
                size + 
                rand.uniform(-1*srand, srand) - 
                (self.lead * SPECIES_LEAD_EFFECT[self.species])
                )
        return x

    def rotate(self, angle=None):
        if not angle: angle=2*pi*rand.random()
        c, s = np.cos(angle), np.sin(angle)
        rot_mat = np.array([[c, -s], [s, c]])
        self.corners = np.array([np.dot(x, rot_mat) for x in self.corners])

    def translate(self, shift=None):
        if not shift: shift = TRANSLATE_SIZE * np.array(
                [rand.uniform(-1,1), rand.uniform(-1,1)])
        self.corners = self.corners + shift
        
    def make_polygon(self):
        pol = Polygon(
                self.corners, 
                color=self.plot_color,
                alpha=0.4
                )
        self.polygon = pol

    def find_diagonals(self):
        c = self.corners
        diags = tuple(
                np.linalg.norm(p2-p1) 
                for (p1,p2) in ((c[2], c[0]), (c[3], c[1]))
                )
        return diags



