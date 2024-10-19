from manim import *
from planet import Planet

class GravitInteraction(Scene):
    def construct(self):
        '''PARAMETERS'''
        #list of planets (arguments : scene instance, id, mass, initial x, initial y)
        planets = [Planet(self,0,3,-3,0),Planet(self,2,5,-1,1),Planet(self,1,1,1,1)]
        #time interval between two images
        dt = 0.1
        #total duration of the animation
        duration = 5

       '''ANIMATION'''
        t = 0
        while t <= duration:
            for planet in planets:
                planet.update_v(planets,dt)
            
            for planet in planets:
                planet.collide(planets)
            
            for planet in planets:
                planet.update_pos(dt)
            self.wait(dt)
            t += dt
            
