#!/usr/local/bin/sage -python
# -*- coding: utf-8 -*-

import sys
import time
from sage.all import *

from kuh96.foucault import *

R1 = 0.4
R2 = 1.0
TH = 2*pi

Pm = PaperModel(R1,R2,TH)
Plots = Graphics()

# 枠
Plots += Pm.border()

# 振り子の中心を示す円
Rarrow = 0.8
Plots += Pm.arc(Rarrow) # , thickeness=1)

# 振り子を示す矢印
Anum = 12
Adelta = 2*pi/Anum
Plots += Pm.parrows(Anum, 0, Adelta,  \
                   Rarrow, 0.12, 0, \
                    color='limegreen', zorder=100)

# 緯度を示す半径線
LatNum = 9
Plots += Pm.latitudes(LatNum, 0, pi/LatNum/2, 0.95)

# 保存、表示
Outfile = "../out/paper-model.png"
Plots.save(Outfile, axes=False)
Plots.show(filename=Outfile, axes=False)
# raw_input("Enter return to exit..")

