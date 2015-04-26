#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
import time
from sage.all import *
from sage.plot.plot3d.parametric_surface import ParametricSurface
from sage.plot.plot3d.shapes2 import Line

from kuh96.foucault import *

'''
Latitude = 50
BaseTh = 2*pi*sin(Latitude*pi/180)
ConeTh = 2*pi
con = ConicSector(1, BaseTh, ConeTh)
frame = point3d([-1,-1,-1]) + point3d([1,1,1]) # サイズを一定にするため
p = Graphics()
p += con.surf(0.5, 1, color='lightgreen', opacity=0.8)
p += con.arc(0.75)
p.show()

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
'''

Outfile = "../out/50deg.gif"
Latitude = 50
a = ConicSector.anime(Latitude)
print "saving.."
a.gif(savefile=Outfile, delay=100, iterations=1)
print "end"

Outfile = "../out/north-pole.gif"
Latitude = 90
a = ConicSector.anime(Latitude)
print "saving.."
a.gif(savefile=Outfile, delay=100, iterations=1)
print "end"

