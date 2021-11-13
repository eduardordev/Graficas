from formas import *

SKY_BLUE = color(77,166,255)
YELLOW = color(255, 255, 200)
BROWN = color(98, 42, 4)
GREEN = color(77, 102, 0)
LIGHT_PURPLE = color(80, 80, 120)
BABY_BLUE = color(150, 180, 200)

ivory = Material(diffuse=YELLOW, albedo=(0.6, 0.3, 0.1, 0), spec=50)
wood = Material(diffuse=BROWN, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
leaf = Material(diffuse=GREEN, albedo=(1, 1, 0, 0), spec=50, refractive_index=0)
water = Material(diffuse=LIGHT_PURPLE, albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
glass = Material(
    diffuse=BABY_BLUE,
    albedo=(0, 0.5, 0.1, 0.8),
    spec=125,
    refractive_index=1.5,
)
