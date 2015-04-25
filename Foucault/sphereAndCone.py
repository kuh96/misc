#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *

# 平面のパラメータ表示の関数 func(u,v) を返す。
# 点の座標(x,y,z) と、２つの線形独立なベクトル t1, t2 を指定する。
def planeFunc(pt, t1, t2):
    def func(u, v):
      vxyz =  pt + t1*u + t2*v
      print vxyz
      return (vxyz[0], vxyz[1], vxyz[2])

    return func

# 接平面のパラメータ表示の関数 func(u,v) を返す。
# 曲面のパラメータ表示の関数 surf(u,v) と
# 接点の座標 (u0,v0), 
def tangentPlaneFunc(surf, uv0):
    return

W = 1.5
sph = surfaces.Sphere()
plots = sph.plot()
plots += point3d([-W,-W,-W]) + point3d([W,W,W])

u0 = (90-50)/180*pi
v0 = pi/4
spt0 = vector([u0,v0])

tv1 = sph.tangent_vector(spt0, (1,0))
tv2 = sph.tangent_vector(spt0, (0,1))

x = sph.equation[0](u0,v0)
y = sph.equation[1](u0,v0)
z = sph.equation[2](v0)
point = vector([x,y,z])
func = planeFunc(point, tv1, tv2)

u, v = var('u,v')
pw = 0.5
tplane = parametric_plot3d(func(u,v), (-pw, pw), (-pw,pw), \
  boundary_style={"color": "black", "thickness": 2},  \
  opacity=0.7, color='yellow')

plots += tplane
plots.show(axes=True, frame=False, language='en')


