'''
Created on Jun 4, 2012

@author: kan
'''
from shapely.geometry import Polygon
from random import *
import pylab
import numpy as np



def point_generator(polygon, p1, p2):
    midx = (p1[0] + p2[0])/2.0
    midy = (p1[1] + p2[1])/2.0
    #r = numpy.random.standard_normal((2,1))
    while True:        
        dx = gauss(0,1)
        dy = gauss(0,1)
        p3 = midx + dx, midy + dy
        triangle = Polygon([p1, p2, p3])
        un = polygon.union(triangle)
        if un.area == polygon.area + triangle.area:
            return p3
def seg_p_dis(p1, s1, s2):
    c = np.array(p1)
    b = np.array(s1)
    a = np.array(s2)
    k = np.sum((c-a)*(b-a))/np.sum((a-b)*(a-b))
    k = max(0,k)
    k = min(1,k)
    orth = a + k * (b-a)
    orth = orth[0],orth[1]
    return orth, np.sum((a-orth)*(a-orth))**.5


def random2d(m=0, var=1):
    return gauss(m,var),gauss(m,var)
# this method can generator a sequence with n triangles
def tri_generator(n):
    a = random2d()
    b = random2d()
    c = random2d()
    tlist = [(0, 1, 2)]
    plist = [a, b, c]
    trisequence = Polygon(plist)
    id = [1, 2]
    pcount = 2
    
    #initialization of the greedy path
    enterance = a[:]
    enterance , dis = seg_p_dis(enterance, b, c)
    greedy = dis
    elist = [enterance]
    #start routing
    for i in range(n-1):
        pcount = pcount + 1
        new = point_generator(trisequence, plist[id[0]], plist[id[1]])
        tri = Polygon([plist[id[0]], plist[id[1]], new])
        trisequence = trisequence.union(tri)
        tlist.append((id[0],id[1],pcount))
        plist.append(new)        
        id[randint(0,1)] = pcount
        if i< n-2 :
            enterance, dis = seg_p_dis(enterance, plist[id[0]], plist[id[1]])
            elist.append(enterance)
        else:
            dis = sum([(enterance[i]-new[i])**2 for i in range(2)])**.5
            elist.append(new)
        greedy = greedy + dis
    return plist, tlist, elist, greedy 

plist, tlist, el, glength = tri_generator(10)
x = [plist[i][0] for i in range(len(plist))]
y = [plist[i][1] for i in range(len(plist))]


ex = [el[i][0] for i in range(len(el))]
ey = [el[i][1] for i in range(len(el))]


x = np.array(x)
y = np.array(y)
ex = np.array(ex)
ey = np.array(ey)
for t in tlist:
    t_i = [t[0], t[1], t[2], t[0]]
    pylab.plot(x[t_i], y[t_i])
pylab.plot(x, y, 'o')

l = list(range(len(el)))
pylab.plot(ex[l], ey[l])

pylab.plot(ex, ey, 'o')


pylab.show()


    



        
                    
        
    
