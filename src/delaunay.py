'''
Created on Jun 4, 2012

@author: kan
'''
import matplotlib.delaunay as triang
import pylab
import numpy

# 10 random points (x,y) in the plane
x,y =  numpy.array(numpy.random.standard_normal((2,10)))
cens,edg,tri,neig = triang.delaunay(x,y)

for t in tri:
    # t[0], t[1], t[2] are the points indexes of the triangle
    t_i = [t[0], t[1], t[2], t[0]]
    pylab.plot(x[t_i],y[t_i])

pylab.plot(x,y,'o')
pylab.show()