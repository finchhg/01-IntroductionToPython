"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Harrison Finch.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window =rg.TurtleWindow()

jim = rg.SimpleTurtle('turtle')
jim.pen = rg.Pen('Pink', 20)
jim.speed = 20
print('20')
size = 500

for k in range(20):
    jim.draw_square(100)
    jim.right(45)
    jim.forward(89)

bob = rg.SimpleTurtle('turtle')
bob.pen = rg.Pen('Green', 10)
bob.speed=30

for k in range(50):

    bob.draw_circle(25)
    bob.left(57)
    bob.backward(23)
    bob.speed=100

jim.go_to(rg.Point(-100,200))
bob.go_to(rg.Point(-100,200))

window.close_on_mouse_click()
