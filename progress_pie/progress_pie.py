#!/usr/bin/python3
import math
import sys


RADIUS = 50
TOLERANCE = 1e-6


def check (x, y, p):
    #print("p: {} , (x,y) : ({},{})".format(p,x,y))
    colors = {False: 'white', True: 'black'}

    def in_line (x, y, p):
        if p == 0:
            return False

        p_angle = p*math.pi*2/100
        beta = math.pi/2 - math.atan2(y-RADIUS, x-RADIUS)
        if beta < 0:
            beta += math.pi*2

        #print("(percentage) " + str(p_angle) + " >>>>> (point) " + str(beta))
        return beta < p_angle

    def in_circle (x, y):
        #print("({} + {})^0.5 = {} < {}".format((x-RADIUS)**2, (y-RADIUS)**2, ((x-RADIUS)**2 + (y-RADIUS)**2)**0.5, RADIUS))
        return ((x-RADIUS)**2 + (y-RADIUS)**2)**0.5 <= RADIUS

    return colors[in_circle(x,y) and in_line(x,y,p)]


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
