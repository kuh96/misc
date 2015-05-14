#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *
from sage.plot.plot3d.parametric_surface import ParametricSurface
from sage.plot.plot3d.shapes2 import Line

def simplifyFull(list):
    return [x.simplify_full() for x in list]

class PaperModel:
    '''
    扇形を作成。内側の半径 R1 外側の半径 R2 中心角 TH
    '''
    def __init__(self, R1, R2, TH):
        self.R1 = R1; self.R2 = R2; self.TH=TH

    '''
    放射状の半径線の　plot を得る。
    角度の位置 phi, ラベル文字列 str
    ラベルの半径方向の位置 rlabel,
    半径線に対するラベルの角度 dphi
   '''
    def radiusLine(self, phi, str, rlabel, dphi, **kws):
        r = var('r')
        line = parametric_plot([r*cos(phi), r*sin(phi)], \
                               (r,self.R1,self.R2), **kws)
        pp = phi + dphi
        if str != "" :
            txt = text(str, (rlabel*cos(pp),rlabel*sin(pp)), \
                       rotation=180/pi*pp + 90)
            return line + txt
        else:
            return line

    def border(self, **kws):
        phi = var('phi')
        p = polar_plot(self.R1  ,(phi, 0, self.TH), thickness=2, **kws)
        p += polar_plot(self.R2 ,(phi, 0, self.TH), thickness=2, **kws)
        p += self.radiusLine(0, "", self.R1+0.2, 0, thickness=2, **kws)
        return p

    def arc(self, r, **kws):
        phi = var('phi')
        p = polar_plot(r, (phi, 0, self.TH), **kws)
        return p

    '''
    緯度を示す半径線とラベルを書く
    '''
    def latitudes(self, num, lat1, delta, rlabel, **kws):
        p = Graphics()
        for n in raimnge(num):
            lat = lat1 + n * delta
            p += self.radiusLine(2*pi*sin(lat), \
                       u"%2d°" % (180*lat/pi),\
                       rlabel, 0.05, linestyle='dotted', **kws)
        return p
        
    '''
    (r,phi)を中心に、長さ2*len 角度 X軸に対しrot の矢印を書く
    '''
    def parrow(self, r, phi, len, rot, **args):
        x = r*cos(phi); y = r*sin(phi);
        dx = len*cos(rot); dy = len*sin(rot);
        line = arrow((x - dx,y-dy),(x + dx, y+dy), **args)
        return line
    
    def parrows(self, num, phi0, dphi, r, len, rot, **args):
        p = Graphics()
        for n in range(num):
            phi = phi0 + n*dphi
            p += self.parrow(r, phi, len, rot, **args)
        return p

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
        coords = ((r, r1, r2), (th, 0, self.TH))
        surf = ParametrizedSurface3D(self.xyz(r,th),  \
                                     coords, 'cone sector')
        return surf
    
    def spoke(self, r1, r2, th, **args):
        r = var('r')
        a = parametric_plot3d( self.xyz(r,th), (r1, r2), **args)
        return a
    
    def pline(self, surf, r, th, len, phi, n, **args):
        at = (r,th)
        dir = (cos(phi-th), sin(phi-th))
        t1 = surf.tangent_vector(at, dir)
        t1 = t1 / abs(t1);
        p0 = self.xyz0(at)
        p1 = p0 + len*t1
        p2 = p0 - len*t1

        t = var('t')
        eq = p1*t + p2*(1-t)
        a = parametric_plot3d(eq, \
                               (0,0.5), color='red', thickness=5, **args)
        b = parametric_plot3d(eq, \
                              (0.5,1), color='green', thickness=5, **args)
        return a+b;

    def equation(self):
        r = var('r'); th = var('th')
        rr = r*self.A; thh = th/self.A
        r,th = var('r,th')
        return (rr*cos(thh), rr*sin(thh), (self.R - r)*sqrt(1-self.A**2))

    def surface(self, rrange=None, thrange=None, **kws):
        r = var('r'); th = var('th')
        if rrange == None:
            rrange = (r, 0, self.R)
        if thrange == None:
           thrange = (th, 0, self.TH)

        coords = (rrange, thrange)
        surf = ParametrizedSurface3D(self.equation(), coords, 'cone sector')
        return surf

    def xyz(self, r, th):
        rr = r*self.A; thh = th/self.A
        x = rr*cos(thh)
        y = rr*sin(thh)
        z = (self.R - r)*sqrt(1-self.A**2)
        return (x,y,z)
    
    def xyz0(self, rth):
        return vector(self.xyz(rth[0], rth[1]))

    def xyzFromXY(self, x, y, n):
        # TODO: incomplete!
        r = sqrt(x**2 + y**2)
        th1 = atan2(y, x)
        if th1 < 0:
            th1 = 2*pi + th1
        th = 2*pi*n + th1
        print "  n,th1,th", n, th1.n(), th.n()
        return self.xyz(r, th)

    '''
    緯度と、図の回転（軸の方向と角度）を指定
    '''
    @staticmethod
    def anime(latitude, coneTh=2*pi, rotaxis=(1,1,0), angle=(-pi/2+0.9), linedir=0):
        baseTh = 2*pi*sin(latitude*pi/180)
        con = ConicSector(1, baseTh, coneTh)
        frame = point3d([-1,-1,-1]) + point3d([1,1,1]) # サイズを一定にするため
        surf = con.surf(0.5, 1)
        p = Graphics()
        p += surf.plot(color='lightgreen', opacity=0.8, \
                       boundary_style={"color": "black", "thickness": 2})
        p += con.arc(0.75)

        for i in range(6):
            p += con.spoke(0.5, 1, i*con.TH/6)

        anime = []
        linelen = 0.2 # 線の長さ 
        # linedir = 0  # 線とX軸の角度 TODO: pi/2 にするとおかしくなるバグ
        for i in range(13):
            th = i*con.TH/6
            n = int(th/2/pi);
            pp = p + con.pline(surf, 0.75, th, linelen, linedir, n)
            pp = pp.rotate((1,1,0), (-pi/2 + 0.9)) + frame
            anime.append(pp)

        a = animate(anime, frame=False)
        return a

print "loaded foucault.py"

if __name__ == '__main__':
    print "executing foucault.py"

    R = var('R')
    TH = var('TH')
    THH = var('THH')
    con = ConicSector(R, TH, THH)
    e = con.equation()
    print e

    RR=0.5
    con = ConicSector(1, pi*6/4, pi*7/4)
    e = con.equation()
    print e

    r, th = var('r,th', domain='real')
    surf = con.surface()
    surf.plot().show()

    raw_input('..')

