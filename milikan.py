from pylab import plot,show
from numpy import loadtxt,size,linspace, arange, array
from math import *

data = loadtxt("millikan.txt",float)
x = data[:,0]
y = data[:,1]
N = 6
Ex = sum(x)/N
Ey = sum(y)/N
Exx = sum(x*x)/N
Exy = sum(x*y)/N
m = (Exy - Ex * Ey)/(Exx - Ex * Ex)
c = (Exx * Ey - Ex * Exy)/(Exx - Ex * Ex)
# computation of m and c

e = 1.602e-19
h = m * e
# computation of h

print "m=",m,"c=",c
print "h=",h
# print out values we obtained

xl = array(x)
# store xi in array
yl = array(m * x + c)
# store mxi + c in array

plot(x,y,"k.")
# show the experimental data
plot(x,yl,"k-")
# show the least-squares fitted line
show()
