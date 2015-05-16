#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
from sage.all import *

class PlaneCurve:
    '''
    曲線のパラメータ変数名と、曲線の式 x(p), y(p) を指定
    '''
    def __init__(self, variable, xeq, yeq, name="plane curve"):
        self.variable = variable
        self.eq = vector([xeq,yeq])
        self.name = name

    '''
    描画用に曲線のパラメータ以外の変数の値をセットする
    '''
    def setParams(self, **params):
        self.params = params

    '''
    セットしたパラメータ値でベクトルの式をセットする
    '''
    def eval(self, vec):
        f = vector([vec[0](**self.params), vec[1](**self.params)])
        return f

    '''
    パラメータ範囲を指定して曲線の parametric_plot を得る
    '''
    def plot(self, t0, t1, **kws):
        funcs = self.eval(self.eq)
        return parametric_plot(funcs, (self.variable,t0,t1), **kws)

    '''
    num 個のフレームの plot を得る
    '''
    def plotFrames(self, t0, t1, num, **kws):
        delta = (t1 - t0)/num;
        tvar = self.variable
        plot = Graphics()
        for i in range(num):
            t = t0 + i*delta
            pt = self.eval(self.eq)({tvar: t})
            (tan,nor) = self.frame()
            tt = tan({tvar: t}); nn = nor({tvar: t})
            tt = tt/abs(tt); nn = nn/abs(nn)
            print "  N, t, tan, nor:", i, t, tt, nn
            ta = arrow(pt, pt+tt, color='green')
            tb = arrow(pt, pt+nn, color='black')
            plot += ta + tb

        return plot

    def tangent(self):
        return diff(self.eq, self.variable)

    def normal(self):
        return diff(self.eq, self.variable, 2)

    '''
    パラメータ値をセットしたフレームを得る
    '''
    def frame(self):
        t = self.tangent()
        n = self.normal()
        print "  t,n=", t, n
        print "  params=", self.params
        tf = self.eval(t)
        nf = self.eval(n)
        return (tf, nf)


print "loaded plane.py"

if __name__ == '__main__':
    print "executing plane.py"

    r, th = var('r, th')
    curve = PlaneCurve(th, r*cos(th), r*sin(th), 'circle')
    curve.setParams(r=2)
    print "funcs=", curve.eval(curve.eq)
    print "tan=", curve.tangent()
    print "nor=", curve.normal()
    print "frame=", curve.frame()
    plot = curve.plot(0, 2*pi)
    plot += curve.plotFrames(0, 2*pi, 20);
    plot.show()
    
    a,b = var('a,b')
    curve = PlaneCurve(th, a*cos(th), b*sin(th), 'ellipse')
    curve.setParams(a=3, b=1.8)
    print "funcs=", curve.eval(curve.eq)
    print "tan=", curve.tangent()
    print "nor=", curve.normal()
    print "frame=", curve.frame()
    plot = curve.plot(0, 2*pi)
    plot += curve.plotFrames(0, 2*pi, 20);
    plot.show()

    raw_input("..")
