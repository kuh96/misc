#!/usr/local/bin/sage -python

import sys
from sage.all import *

from sage.plot.plot3d.parametric_surface import ParametricSurface
from sage.plot.plot3d.shapes2 import Line

def map(**args):
    return args

class ConicSector:
    def __init__(self, R, TH, THH):
        self.R = R; self.TH=TH; self.THH=THH; self.A = self.TH/self.THH

    def radius(self):
        return self.R * self.A

    def height(self):
        return self.R * sqrt(1 - (self.A)**2)

    def arc(self, r, **args):
        th = var('th')
        a = parametric_plot3d(self.xyz(r,th), (0, self.TH),  **args)
        return a

    def surf(self, r1, r2, **args):
        r, th = var('r,th')
        a = parametric_plot3d(self.xyz(r,th), (r, r1, r2), (th, 0, self.TH), \
            boundary_style={"color": "black", "thickness": 2},  **args)
        return a
    
    def spoke(self, r1, r2, th, **args):
        th = self.thmod(th)
        r = var('r')
        a = parametric_plot3d( self.xyz(r,th), (r1, r2), **args)
        return a
    
    def line(self, r, th, len, phi, **args):
        th = self.thmod(th)
        x = r*cos(th); y = r*sin(th)
        x1 = x + len*cos(phi); y1 = y + len*sin(phi); p1 = self.xyzFromXY(x1, y1)
        x2 = x - len*cos(phi); y2 = y - len*sin(phi); p2 = self.xyzFromXY(x2, y2)
        # print p1, p2
        t = var('t')
        a = parametric_plot3d([p1[0]*t + p2[0]*(1-t), \
                               p1[1]*t + p2[1]*(1-t), p1[2]*t + p2[2]*(1-t)], \
                               (0,0.5), color='red', thickness=5, **args)
        b = parametric_plot3d([p1[0]*t + p2[0]*(1-t), p1[1]*t + p2[1]*(1-t), 
                               p1[2]*t + p2[2]*(1-t)], \
                              (0.5,1), color='blue', thickness=5, **args)
        return a+b;
    
    def thmod(self, th):
        return th - int(th/self.TH)*self.TH
    

    def xyz(self, r, th):
        rr = r*self.A; thh = th/self.A
        return (rr*cos(thh), rr*sin(thh), (self.R-r)*sqrt(1-self.A**2))
    
    def xyzFromXY(self, x, y):
        r = sqrt(x**2 + y**2); th=RDF(arccos(x/r))
        if y < 0: th=RDF(2*pi - th)
        
        # print x.n(),y.n(),(th).n()
        return self.xyz(r, th)

    def atan(x,y):
        th = arctan(y/x)
        if th < 0:
            return pi + th
        else:
            return th

#
from sage.plot.plot3d.shapes2 import frame3d, point3d
#args = {'aspect_ratio':1}
args = map(aspect_ratio=1, frame=False, axes=False, viewer='tachyon')

ATHH = 2*pi*sin(50*pi/180)
con = ConicSector(1, ATHH, ATHH)
frame = point3d([-1.1,-1.1, -1.1]) + point3d([1.1,1.1,1.1])

p = Graphics()
p += con.surf(0.5, 1, color='lightgreen', opacity=0.8)
# p += con.spoke(0,1,0)
p += con.arc(0.75)

for i in range(6):
    p += con.spoke(0.5, 1, i*con.TH/6)

anime = []
for i in range(6):
    anime.append( p + con.line(0.5, i*con.TH/6, 0.1, 0) + frame)

a = animate(anime)
# a.show(delay=100, iterations=4)

anime = []
for i in range(25):
    th = con.thmod(i*con.TH/12); print th
    pp = p + con.line(0.75, th, 0.1, 0)
    pp = pp.rotate((1,1,0), (-pi/2 + 0.9)) + frame
    anime.append(pp);

a = animate(anime)

print "showing.."
#a.show(delay=100, iterations=4, frame=False)
a.gif(savefile="out/anime.gif", delay=100, iterations=4)
#a.save(filename="out/anime.gif", delay=100, iterations=4)
print "end"
