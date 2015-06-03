# Use a Piece of Paper, to Understand the Foucault Pendulum 

Understanding the rotation of the Foucault Pendulum is not difficult.
A piece of paper is enough for you! 

* [original in Japanese](http://qiita.com/kuh96/items/a4b0816875fee3684dc4)

### Cut out the figure along the bold lines

<img src="out/paper-model.png" width="30%" />

### Then, build it up into a cone!

* Each radial line and label (xx degrees) designates the latitude where you want to observe the rotaion of the pendulum.
* For example, overlay the 0-degree edge on top of the 50-degree line, and fix the sheet with a clip.
<img src="out/buildUp.gif" width="30%" />

### Completed !

<img src="etc/completed.JPG" width="30%" />

- Rotate the paper model and look at the arrow that comes in front of you
- Or rotate yourself around the model!

### Animation - Rotation at 50 degrees north latitude

<img src="out/50deg.gif" width="30%" />

### Why?

- Obviously the pendulum does not rotate near the North Pole
 - It's only the ground that rotates
 - The pendulum simply translates in parallel

<img src="out/north-pole.gif" width="30%" />

- In the mid-latitudes, the ground is inclined with respect to the earth's axis
- The pendulum moves along a conical surface consequently

<img src="out/cone.png" width="30%" />

- Surely the pendulum will move in parallel on this conical surface!
- Luckily a conical surface is developable. It can be flattened into a plane!

So:

|| Draw parallel lines on a plane sheet | Bend the sheet into a conical surface, then you get the rotation of the Foucault pendulum! |
|:-----:|:-----:|:-----:|
|5o degrees| <img src="out/flat50deg.gif" width="50%" /> | <img src="out/50deg.gif" width="50%" /> |
|30 degrees| <img src="out/flat30deg.gif" width="50%" /> | <img src="out/30deg.gif" width="50%" /> |

# Fixed bugs (2015-05-14)

|fixed|old bug|
|:-----:|:-----:|
|<img src="out/fixed-bug.gif" width="30%" />|<img src="out/known-bug.gif" width="30%" />|


# Acknowledgment

This is my first development using **[SageMath](http://www.sagemath.org)** and Python.
Thanks to the great tools !

<img src="etc/dev.JPG" width="30%" />




