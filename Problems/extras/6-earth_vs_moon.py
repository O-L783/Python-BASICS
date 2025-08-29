######################################################################
#
# Earth vs Moon
#
# The surface area of the earth is 5.1 x 10^8 sq km, and
# 71% of the earth's surface is covered in water.
#
# The diameter of the moon is 3,475 km, and there is no
# liquid water on the surface of the moon.
#
# Which has more dry land, the earth or the moon?
#
# [Quiz question from Time magazine]


# First calculate the amount of dry land on the earth,
# truncated to a whole number

earths_surface_area = 5.1 * (10 ** 8) # sq km

earths_water_area = earths_surface_area * 0.71

earths_dry_land = int(earths_surface_area - earths_water_area)


# Now calculate the moon's surface area, also as a whole number
#
# Remember that the surface area of a sphere is
# 4 times pi times r squared

moons_radius = 3475 / 2 # km

from math import pi

moons_surface_area = 4 * pi * (moons_radius ** 2) # sq km

moons_dry_land = int(moons_surface_area)


# Now display the results as two character strings

print('Earth: ' + str(earths_dry_land) + ' sq km of dry land')
print('Moon:   ' + str(moons_dry_land) + ' sq km of dry land')

