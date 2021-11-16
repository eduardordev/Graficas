from formas import *

SKY_BLUE = color(77,166,255)
SKIN = color(254,228,213)
SKIN1 = color(218,180,157)
BROWN = color(98, 42, 4)
GREEN = color(77, 102, 0)
LIGHT_PURPLE = color(80, 80, 120)
BABY_BLUE = color(150, 180, 200)
ORANGE = color(245,149,29)
ORANGE1 = color(238,136,26)
ORANGE2 = color(230,126,29)
ORANGE3 = color(224,114,25)
ORANGE4 = color(202,82,21)
ORANGE5 = color(208,91,21)
ORANGE6 = color(216,105,26)
ORANGE7 = color(158,33,29)
ORANGE8 = color(237,136,32)
ORANGE9 = color(232,130,32)
ORANGE10 = color(226,118,27)

skin = Material(diffuse=SKIN, albedo=(0.6, 0.3, 0.1, 0), spec=50)
skin1 = Material(diffuse=SKIN1, albedo=(0.6, 0.3, 0.1, 0), spec=50)
orange = Material(diffuse=ORANGE, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange1 = Material(diffuse=ORANGE1, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange2 = Material(diffuse=ORANGE2, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange3 = Material(diffuse=ORANGE3, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange4 = Material(diffuse=ORANGE4, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange5 = Material(diffuse=ORANGE5, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange6 = Material(diffuse=ORANGE6, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange7 = Material(diffuse=ORANGE7, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange8 = Material(diffuse=ORANGE8, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange9 = Material(diffuse=ORANGE9, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange10 = Material(diffuse=ORANGE10, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)

leaf = Material(diffuse=GREEN, albedo=(1, 1, 0, 0), spec=50, refractive_index=0)
water = Material(diffuse=LIGHT_PURPLE, albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
glass = Material(
    diffuse=BABY_BLUE,
    albedo=(0, 0.5, 0.1, 0.8),
    spec=125,
    refractive_index=1.5,
)
