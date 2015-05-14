#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
import time
from sage.all import *
from kuh96.foucault import *

if True:
    Outfile = "../out/50deg.gif"
    Latitude = 50
    a = ConicSector.anime(Latitude, linedir=0)
    print "saving..", Outfile
    a.gif(savefile=Outfile, delay=100, iterations=0)
    print "end"

if True:
    Outfile = "../out/flat50deg.gif"
    Latitude = 50
    ConeTh = 2*pi*sin(Latitude*pi/180)
    a = ConicSector.anime(Latitude, coneTh=ConeTh, linedir=0)
    print "saving..", Outfile
    a.gif(savefile=Outfile, delay=100, iterations=0)
    print "end"

if True:
    Outfile = "../out/north-pole.gif"
    Latitude = 90
    a = ConicSector.anime(Latitude, linedir=0)
    print "saving..", Outfile
    a.gif(savefile=Outfile, delay=100, iterations=0)
    print "end"

if False:
    Outfile = "../out/30deg.gif"
    Latitude = 30
    a = ConicSector.anime(Latitude, linedir=0)
    print "saving..", Outfile
    a.gif(savefile=Outfile, delay=100, iterations=0)
    print "end"

if False:
    Outfile = "../out/flat30deg.gif"
    Latitude = 30
    ConeTh = 2*pi*sin(Latitude*pi/180)
    a = ConicSector.anime(Latitude, coneTh=ConeTh, linedir=0)
    print "saving..", Outfile
    a.gif(savefile=Outfile, delay=100, iterations=0)
    print "end"

if False:
    Outfile = "../out/fixed-bug.gif"
    Latitude = 50
    ConeTh = 2*pi*sin(Latitude*pi/180)
    a = ConicSector.anime(Latitude, linedir=pi/2)
    print "saving..", Outfile
    a.gif(savefile=Outfile, delay=100, iterations=0)
    print "end"


