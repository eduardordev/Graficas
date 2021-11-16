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



skin = Material(diffuse=SKIN, albedo=(0.6, 0.3, 0.1, 0), spec=50)
skin1 = Material(diffuse=SKIN, albedo=(0.6, 0.3, 0.1, 0), spec=50)
orange = Material(diffuse=ORANGE, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange1 = Material(diffuse=ORANGE1, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange2 = Material(diffuse=ORANGE2, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
orange3 = Material(diffuse=ORANGE3, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)


leaf = Material(diffuse=GREEN, albedo=(1, 1, 0, 0), spec=50, refractive_index=0)
water = Material(diffuse=LIGHT_PURPLE, albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
glass = Material(
    diffuse=BABY_BLUE,
    albedo=(0, 0.5, 0.1, 0.8),
    spec=125,
    refractive_index=1.5,
)
