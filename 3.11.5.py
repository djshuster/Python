# Last updated 13 July, 2020
# Created by David Shuster

# This program draws a fractal-esque tree.

# Potential additions: some sort of algorithm to calculate formulas for length to make the tree screen-fitting,
# (and the possibility of changing the angle within the recursive call...)
# Inspired by Problem 3.11.5 from Data Structures and Algorithms with Python by Kent Lee et al.
import turtle

def main():
    def drawSquare(t):
        t.fillcolor("#00FF00")
        t.begin_fill()
        t.right(90)
        t.forward(2)
        t.left(90)
        t.forward(4)
        t.left(90)
        t.forward(4)
        t.left(90)
        t.forward(4)
        t.left(90)
        t.forward(2)
        t.end_fill()

    def drawBranch(t, angle, numSB): #receives turtle, angle, and number of strict sub-branches
        t.width(numSB)
        if(numSB==0):
            t.forward(eval(lengthString))
            drawSquare(t)
            t.left(90)
        else:
            t.forward(eval(lengthString))
            t.left(angle)
            drawBranch(t, angle, numSB-1)
            t.right(2*angle)
            drawBranch(t, angle, numSB-1)
            t.left(angle)
        t.penup()
        t.back(eval(lengthString))
        t.pendown()

    t=turtle.Turtle()
    t.speed(0)

    rootx = 0
    rooty = -100
    angle = 20 #angle of the first non-trunk branch off of the vertical
    lengthString = "10*numSB+10"
    subBranches = 7 #number of sub-branches off of the tree

    #set-up work
    t.pencolor("#A52A2A")
    t.left(90)
    t.penup()
    t.setposition(rootx, rooty)
    t.pendown()

    drawBranch(t, angle, subBranches)
    turtle.done()

if __name__ == "__main__":
    main()