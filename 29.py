# Exercise No.29

# Create a function that calculates the amount a sphere is filled


# Solution
import math


def part_vol_sphere(h, r=10):
	return (4 * math.pi * r ** 3) / 3 - math.pi * h ** 2 * (3 * r - h) / 3


print(part_vol_sphere(2))
