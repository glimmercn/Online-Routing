'''
Created on Jun 5, 2012

@author: kan
'''
from shapely.geometry import Polygon
from random import *
import pylab
import numpy as np
'''this function gives the closest point on a segment to a given point and their distance.'''
def seg_p_dis(p1, s1, s2):
    c = np.array(p1)
    a = np.array(s1)
    b = np.array(s2)
    k = np.sum((c-a)*(b-a))/np.sum((a-b)*(a-b))
    k = max(0,k)
    k = min(1,k)
    orth = a + k * (b-a)
    orth = orth[0],orth[1]
    return orth, np.sum((a-orth)*(a-orth))**.5

