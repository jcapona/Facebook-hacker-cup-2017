#!/usr/bin/python
from numpy.polynomial.polynomial import polypow
from numpy import ones
import sys
import re

def magic(sides, dices, health, points):
    # Prob of getting a sum of k is the coefficient of x^k in
    # ((x + x^2 + ... + x^m)/m)^n
    # m = sides per dice
    # n = number of dices

    p = ones(sides + 1)
    p[0] = 0
    p /= sides
    p = polypow(p, dices)
    # Get cumulative sum to get prob
    cdf = p.cumsum()
    k = health - points - 1
    return 1 - cdf[k] if k <= len(cdf) and k >0 else 1 if k < 0 else 0


filename = 'fighting_the_zombie_example_input.txt' if len(sys.argv) == 1 else str(sys.argv[1])
regex_move = r"([0-9]+)d([0-9]+)((\+|\-)([0-9]+))?"
reg_move = re.compile(regex_move)

with open(filename, "r") as file:
    line_num = 0
    case = 1
    for line in file:
        if line_num == 0:
            zombies = int(line.split()[0])
        elif (line_num - 1) % 2 == 0:
            health, turn_spells = [int(i) for i in line.split()]
        else:
            prob = []
            for times, sides, points, sign, pts in reg_move.findall(line):
                times = int(times)
                sides = int(sides)
                points = int(points) if points != "" else 0
                prob.append(magic(sides, times, health, points))
                if len(prob) == turn_spells:
                        print("Case #{}: {:0.6f}".format(case, max(prob),6))
                        case += 1
        line_num+=1
