from manim import *
from computations import *

class Planet:
    def __init__(self,scene,id,mass,x0,y0):
        self.id = id
        self.mass = mass
        self.x = x0
        self.y = y0
        self.radius = 0.2*self.mass
        self.mobject = Circle(radius = self.radius,color = GREEN,fill_opacity = 1)
        self.mobject.move_to(RIGHT*self.x + UP*self.y)
        scene.add(self.mobject)
        self.text = Text(str(self.id),height=3/4*0.2*self.mass)
        scene.add(self.text)
        self.vx = 0
        self.vy = 0
    def update_v(self,planets,dt):
        forceX = 0
        forceY = 0

        for planet in planets:
            if planet.id != self.id:
                dist = euclid_dist(self,planet)
                if dist > 0:
                    attraction = get_attraction(self,planet)
                    forceX += get_cos(self,planet) * attraction
                    forceY += get_sin(self,planet) * attraction
        self.vx += (forceX/self.mass)*dt
        self.vy += (forceY/self.mass)*dt
    
    def collide(self,planets):
        for planet in planets:
            if planet.id != self.id:
                if euclid_dist(self,planet) <= (self.radius + planet.radius):
                    self.vx,self.vy = -self.vx*0.5,-self.vy*0.5

    def update_pos(self,dt):
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.mobject.move_to(RIGHT*self.x + UP*self.y)
        self.text.move_to(RIGHT*self.x + UP*self.y)
    
