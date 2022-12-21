from numpy import *

TOP, BOTTOM = range(2)
INSIDE, OUTSIDE = range(2)

def turn_right(vec):
	ret = vec.copy()
	ret[0] = vec[1]
	ret[1] = -vec[0]
	return ret

def turn_left(vec):
	ret = vec.copy()
	ret[0] = -vec[1]
	ret[1] = vec[0]
	return ret

def solve_quadratic(a, b, c):
	t = sqrt(b*b - 4*a*c)
	return (-b + t) / (2*a), (-b - t) / (2*a)

def rad2deg(theta):
	return (theta*360) / (2*pi)

def deg2rad(theta):
	return (theta*2*pi) / 360

def get_intersect(a1, a2, b1, b2):
    """ 
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = vstack([a1,a2,b1,b2])        # s for stacked
    h = hstack((s, ones((4, 1)))) # h for homogeneous
    l1 = cross(h[0], h[1])           # get first line
    l2 = cross(h[2], h[3])           # get second line
    x, y, z = cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return array([x/z, y/z])
