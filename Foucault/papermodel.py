#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *

def rline(phi,r1,r2, str, rr, dphi, **args):
    r = var('r')
    line = parametric_plot([r*cos(phi), r*sin(phi)], (r,r1,r2), **args)
    pp = phi + dphi
    if str != "" :
        txt = text(str, (rr*cos(pp),rr*sin(pp)), rotation=180/pi*pp + 90)
        return line + txt
    else:
        return line

def pline(phi, r, rot, len, **args):
    x = r*cos(phi); y = r*sin(phi);
    dx = len*cos(rot); dy = len*sin(rot);
    line = arrow((x - dx,y-dy),(x + dx, y+dy), **args)
    return line
    

pphi = var('pphi')
th = 2*pi
dth = 0.
p = polar_plot(1,(pphi, -dth, th+dth), thickness=2)
p += polar_plot(0.4 ,(pphi, -dth, th+dth),thickness=2)
p += polar_plot(0.8 ,(pphi, -dth, th+dth),thickness=1)

p += rline(-dth, 0.4,1, "",0,0, thickness=2)
p += rline(th+dth, 0.4,1, "",0,0, thickness=2)

num = 9
delta = pi/num/2
for n in range(num-1):
    lat = n * delta; #print lat
    p += rline(2*pi*sin(lat), 0.4, 1,  u"%2d°" % (180*lat/pi), 0.95, 0.1, linestyle='dotted')

num = 12
delta = 2 * pi/num
for n in range(12):
    p += pline(n*delta, 0.8, pi/2, 0.12, color='limegreen', zorder=1000)

p.save("out/paper-model.png", axes=False)
p.show(axes=False, title="Sample 01")
