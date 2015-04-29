#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
import time
from sage.all import *
from kuh96.foucault import *

Outfile = "../out/buildUp.gif"
Latitude = 50
BaseTh = 2*pi*sin(Latitude*pi/180)
Num = 3
DeltaThh= (2*pi - BaseTh)/Num

frame = point3d([-1,-1, 1],opacity=0) + point3d([1,1, 1],opacity=0) 

anime = []
for i in range(Num+1):
    thh = BaseTh + i*DeltaThh
    con = ConicSector(1, BaseTh, thh);
    surf = con.surf(0.5, 1, color='palegreen');
    anime.append(frame + surf)

a = animate(anime, frame=False, axes=False)
print "saving.."
a.gif(savefile=Outfile, delay=100, iterations=0)
# a.show();
print "end"


# raw_input("..")
