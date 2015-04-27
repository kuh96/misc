#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *
from sage.plot.plot3d.shapes2 import *

def cone(z):
    t = var('t')
    f = z-t
    rev = revolution_plot3d(f,(t,0,1), phirange=(-pi/4, 1.5*pi), \
                            color='yellow', show_curve=True,opacity=0.4)
    arc = revolution_plot3d(f,(t,0.99,1), phirange=(-pi/4, 1.5*pi), \
                            color='red', show_curve=True,opacity=0.9)

    return rev+arc

Plots = Graphics()
Sph = Sphere(1, opacity=0.2)
Plots += Sph
Plots += cone(sqrt(2))
Plots.show(axes=False, aspect_ratio=1, frame=False)
