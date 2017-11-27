"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zheming Zhang.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

Bob = rg.SimpleTurtle('turtle')
Bob.pen = rg.Pen('red',5)
Bob.speed = 15
size = 250

for k in range(3):
    Bob.draw_square(size)
    Bob.pen_up()
    Bob.right(90)
    Bob.forward(20)
    Bob.right(45)
    Bob.forward(50)
    Bob.pen_down()

Rin = rg.SimpleTurtle('turtle')
Rin.pen = rg.Pen('blue',5)
Rin.speed = 15
size = 180

for l in range(8):
    Rin.draw_square(size)
    Rin.pen_up()
    Rin.left(90)
    Rin.forward(20)
    Rin.right(45)
    Rin.forward(50)
    Rin.pen_down()

window.close_on_mouse_click()