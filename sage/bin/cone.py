#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
import time

from sage.all import *
from sage.plot.plot3d.shapes2 import *

def circle():
    return (lambda(t): cos(t), lambda(t): sin(t))

def coneline(lat):
    return lambda(t): (1/cos(lat) - t)/tan(lat)

# 球とそれに接する円錐面
# 緯度、
def sphereAndCone(lat):
    t = var('t')
    coneline = (1/cos(lat) - t)/tan(lat)
    circle = (cos(t), sin(t))
    tt = cos(lat)
    print coneline, circle
    rev = revolution_plot3d(coneline,(t,0, tt+0.1), phirange=(0, 2*pi), \
                            color='yellow', opacity=0.6)
    arc = revolution_plot3d(coneline,(t,tt,tt+0.02), phirange=(0, 2*pi), \
                            color='red', opacity=0.9)
    sph = revolution_plot3d(circle,(t, -pi/2, pi/2), phirange=(0, 2*pi), \
                            color='blue', opacity=0.9)
    return sph + rev + arc

Lat = pi/4
Outfile = "../out/cone.png"
Plots = sphereAndCone(Lat)
Plots.save(Outfile, axes=False, aspect_ratio=1, frame=False)
Plots.show(filename=Outfile, axes=False, aspect_ratio=1, frame=False)

