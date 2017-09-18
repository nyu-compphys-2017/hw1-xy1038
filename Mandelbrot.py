from pylab import imshow, show, gray, colorbar
from numpy import array, empty, ones
from math import *

points = 500
# point number
gap = 4.0/points
# distance of each point in x or y direction
P = ones([points + 1,points + 1], float)
# defining lattice

for m in range(points + 1):
    x = -2.0 + m * gap
    # ergodicity in x direction
    for n in range(points + 1):
        y = -2.0 + n * gap
        # ergodicity in y direction
        c = x + y * 1j
        z = 0.0j + 0.0
        l = 0
        # l is the interation number
        while abs(z) <= 2.0:
            z = z**2 + c
            l = l + 1
            if l >= 100:
                P[n,m] = 0
                break

imshow(P, origin="lower", extent=[-2,2,-2,2])
gray()
colorbar()
show()
