#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *
from sage.plot.plot3d.parametric_surface import ParametricSurface
from sage.plot.plot3d.shapes2 import Line

class ConicalSector:
    def __init__(self, R, TH, THH):
        self.R = R; self.TH=TH; self.THH=THH; self.A = self.TH/self.THH

    def symbolic(self):
        self.A = var('Alpha', latex_name='\\alpha')

    def surface(self, name='Conical sector'):
        r, th = var('r, th')
        rr = r*self.A; thh = th/self.A
        eq = [rr*cos(thh), rr*sin(thh), (self.R - r)*sqrt(1-self.A**2)]
        coords = ((r, 0, self.R), (th, 0, self.TH))
        return ParametrizedSurface3D(eq, coords, name)

print "loaded gbf.py"

if __name__ == '__main__':
    print "executing gbf.py"
    
    con = ConicalSector(1, 3*pi/4, 2*pi)
    surf = con.surface()
    r,th=(0.5, pi/4)
    v1 = surf.tangent_vector((r,th), (1,0))
    v2 = surf.tangent_vector((r,th), (0,1))
    print "v1=", v1
    print "v2=", v2
    
    plot = surf.plot(aspect_ration=1)

#    plot.show()

    raw_input("...")
