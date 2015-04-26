#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *

# パラメータ表示の曲面 surf(u,v) 上の点 (u0,v0) の
# ３次元座標 (x,y,z) を vector で得る
def surfPoint(surf, u0, v0):
    x = surf[0](u=u0,v=v0)
    y = surf[1](u=u0,v=v0)
    z = surf[2](u=u0,v=v0)
    point = vector([x,y,z])
    return point

# 平面を表すパラメータ表示の関数 planeDunc(u,v) を作る。
# 点の３次元vector (x,y,z) と、
# ２つの線形独立な vector t1, t2 を指定する。
def planeFuncCreate(pt, t1, t2):
    def func(u, v):
      vxyz =  pt + t1*u + t2*v
      print " t1,t2,vxyz", t1, t2, vxyz
      return (vxyz[0], vxyz[1], vxyz[2])

    return func

# 接平面のパラメータ表示の関数 func(u,v) を作る。
# 曲面のパラメータ表示の関数 surf(u,v) と
# 接点のパラメータ座標 vector (u0,v0) を指定する。
# TODO: surf(u,v) の変数名を指定可能にすること
def tangentPlaneFuncCreate(surf, u0, v0):
    def tplaneFunc(u,v):
        print "\n  surf=", surf
        dxdu = diff(surf[0], var('u'))(u=u0,v=v0)
        dydu = diff(surf[1], var('u'))(u=u0,v=v0)
        dzdu = diff(surf[2], var('u'))(u=u0,v=v0)
        dxdv = diff(surf[0], var('v'))(u=u0,v=v0)
        dydv = diff(surf[1], var('v'))(u=u0,v=v0)
        dzdv = diff(surf[2], var('v'))(u=u0,v=v0)
        du = vector([dxdu, dydu, dzdu])
        dv = vector([dxdv, dydv, dzdv])
        print "  diff=", du, dv

        point = surfPoint(surf, u0, v0)
        uu,vv=var('uu,vv')
        func = planeFuncCreate(point, du, dv)(u=uu,v=vv)
        print "  u0,v0", u0, v0
        print "  point", point
        print "  tangentPlanefunc=", func
        return func

    return tplaneFunc

def coneFuncCreate(surf, u0, v0):
    def func(t):
        print "cone u0,v0", u0, v0
        tfunc = tangentPlaneFuncCreate(surf, u0, v0)(u=t,v=t)
        print "  coneFunc=", tfunc
        return tfunc

    return func

def sphereCone(surf, th):
    f = coneFuncCreate(surf, 0, th)
    print "  spherefunc=", f
    rev = revolution_plot3d(f, (var('t'), 0, 1))
    return rev

W = 1.5
Sph = surfaces.Sphere()
Surf = Sph.equation
Plots = Sph.plot()
Plots += point3d([-W,-W,-W]) + point3d([W,W,W])

U0 = pi/4 # (90-50)/180*pi
V0 = 0
T = var('T')
Func = coneFuncCreate(Surf, U0, V0)
print "func =", Func(T)
Plots += sphereCone(Surf, U0)

Plots.show(axes=True, frame=False, language='en',  \
perspective_depth=False,  \
           rientation=(0,-1,0)
)

'''
v0 = pi/4
num = 1
dv = 2*pi/num # 2*pi/num

for i in range(num):
    v = v0 + i*dv
    func = tangentPlaneFunc(sph.equation, (u0,v))
    pw = 0.5
    u, v = var('u,v')
    tplane = parametric_plot3d(func(u,v), (-pw, pw), (-pw,pw), \
        boundary_style={"color": "black", "thickness": 2},  \
    opacity=0.7, color='yellow')
    plots += tplane

plots.show(axes=True, frame=False, language='en',  \
perspective_depth=False,  \
           rientation=(0,-1,0)
)
'''


