#!/usr/bin/python3
import math
import sys


RADIUS = 100
TOLERANCE = 1e-6


def check (x, y, p):
    #print("p: {} , (x,y) : ({},{})".format(p,x,y))
    colors = {False: 'white', True: 'black'}

    def in_line (x, y, p):
        alpha = 360*p/100
        beta = 90 - math.atan2(y,x)*360/(2*math.pi)
        #print(str(alpha) + " >? " + str(beta))
        return alpha >= beta

    def in_circle (x, y):
        return x*x + y*y <= RADIUS*RADIUS

    return colors[in_line(x,y,p) and in_circle(x,y)]


filename = 'progress_pie_example_input.txt' if len(sys.argv) == 1 else str(sys.argv[1])
with open(filename, "r") as file:
    num = 0
    solved = 0
    cases = 0
    for line in file:
        if num == 0:
            cases = int(line.split()[0])
        if cases == solved:
            break
        if len(line.split()) > 1:
            p0, x0, y0 = [int(i) for i in line.split()]
            print("Case #" + str(num) + ": " + check(x0, y0, p0))
            solved += 1
        num+=1
