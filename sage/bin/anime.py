#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
import time
from sage.all import *
from kuh96.foucault import *

Outfile = "../out/known-bug.gif"
Latitude = 50
a = ConicSector.anime(Latitude, linedir=2/pi)
print "saving.."
a.gif(savefile=Outfile, delay=100, iterations=1)
print "end"


