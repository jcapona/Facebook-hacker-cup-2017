#!/usr/bin/python3
import sys


MIN_WEIGHT = 50


def get_packages(full_load):
    packages = 0
    package_weight = 0
    items = len(full_load)
    while len(full_load) >= 1:
        max_load = max(full_load)
        package_weight = max_load
        full_load.remove(max(full_load))
        #print("MAX: Removed {}, remains: {}".format(max_load, full_load))
        while package_weight < MIN_WEIGHT and len(full_load) >= 1:
            #print("MIN: will remove {} from : {}".format(min(full_load), full_load))
            full_load.remove(min(full_load))
            package_weight += max_load
        #print("Package weight: {}".format(package_weight))
        if package_weight >= MIN_WEIGHT:
            packages += 1
    return packages


filename = 'lazy_loading_example_input.txt' if len(sys.argv) == 1 else str(sys.argv[1])
with open(filename, "r") as file:
    line_num = 0
    n = 1
    case = 1
    curr_load = []
    expected_size = 0
    for line in file:
        if line_num == 0:
            days = int(line.split()[0])
        elif line_num == n:
            expected_size = int(line.split()[0])
            n += expected_size + 1
        else:
            curr_load.append(int(line.split()[0]))
            if len(curr_load) == expected_size:
                print("Case #{}: {}".format(case, get_packages(curr_load)))
                case += 1
        line_num+=1
