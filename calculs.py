from numpy import *

def euclid_dist(planet1,planet2):
    return sqrt((planet1.x-planet2.x)**2+(planet1.y-planet2.y)**2)

def get_cos(planet1,planet2):
    if euclid_dist(planet1,planet2) > 0:
        return (planet2.x-planet1.x)/euclid_dist(planet1,planet2)
    else:
        return 0
def get_sin(planet1,planet2):
    if euclid_dist(planet1,planet2) > 0:
        return (planet2.y-planet1.y)/euclid_dist(planet1,planet2)
    else:
        return 0

def get_attraction(planet1,planet2):
    G = 1#6.67*10**-11
    if euclid_dist(planet1,planet2) > 0:
        return G*(planet1.mass*planet2.mass)/euclid_dist(planet1,planet2)**2
    else:
        return 0
