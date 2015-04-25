#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *
from sage.plot.plot3d.parametric_surface import ParametricSurface
from sage.plot.plot3d.shapes2 import Line

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
    
    def line(self, r, th, len, phi, n, **args):
        x = r*cos(th); y = r*sin(th)
        x1 = x + len*cos(phi); y1 = y + len*sin(phi);
        p1 = self.xyzFromXY(x1, y1, n)
        x2 = x - len*cos(phi); y2 = y - len*sin(phi);
        p2 = self.xyzFromXY(x2, y2, n)

#        print "x1,y1", x1.n(), y1.n()
        print "  p1", p1[0].n(), p1[1].n(), p1[2].n()
#        print "x2,y2", x2.n(), y2.n()
        print "  p2", p2[0].n(), p2[1].n(), p2[2].n()

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
        x = rr*cos(thh)
        y = rr*sin(thh)
        z = (self.R - r)*sqrt(1-self.A**2)
        return (x,y,z)
    
    def xyzFromXY(self, x, y, n):
        # TODO: incomplete!
        r = sqrt(x**2 + y**2)
        th1 = atan2(y, x)
        if th1 < 0:
            th1 = 2*pi + th1
        th = 2*pi*n + th1
        print "  n,th1,th", n, th1.n(), th.n()
        return self.xyz(r, th)

#
from sage.plot.plot3d.shapes2 import frame3d, point3d

Latitude = 50
BaseTh = 2*pi*sin(Latitude*pi/180)
ConeTh = 2*pi
con = ConicSector(1, BaseTh, ConeTh)
frame = point3d([-1,-1,-1]) + point3d([1,1,1]) # サイズを一定にするため

p = Graphics()
p += con.surf(0.5, 1, color='lightgreen', opacity=0.8)
p += con.arc(0.75)

for i in range(6):
    p += con.spoke(0.5, 1, i*con.TH/6)

anime = []
linelen = 0.2 # 線の長さ 
linedir = 0   # 線とX軸の角度 TODO: これを pi/2 にするとおかしくなるバグ
for i in range(13):
    th = i*con.TH/6
    print i, th.n()
    n = int(th/2/pi);
    pp = p + con.line(0.75, th, linelen, linedir, n)
    pp = pp.rotate((1,1,0), (-pi/2 + 0.9)) + frame
    anime.append(pp);

a = animate(anime)

print "showing.."
a.gif(savefile="out/anime.gif", delay=100, iterations=1)
print "end"
