# Volume of a cylinder
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the measurements of a cylindrical
# tank:

radius = 4 # metres
height = 10 # metres

# Also assume that we have imported the existential constant "pi"
# from the "math" library module:

from math import pi

# Write an expression, or expressions, to calculate the volume
# of the tank.

circle_area = pi * (radius ** 2)
cylinder_vol = circle_area * height

# Print the result in a message to the screen.  (If
# you've forgotten the formula for the area of a circle and hence
# volume of a cylinder, ask one of your workshop partners!)

print("Printing the result in the simplest format.")
print("The volume of the cylinder is ", cylinder_vol, " Cubic Metres\n")

print("Printing the result rounded to two decimal places.")
print("The volume of the cylinder is ", round(cylinder_vol,2), " Cubic Metres\n")

print("An alternate format of the above print statement to make code easier to read")
print("The volume of the cylinder is " +
      str(round(cylinder_vol,2)) +
      " Cubic Metres\n")


print("Printing all the details used and the intermediate steps.")
string_format = (f"Using the formatted output method\n"
                 # Create the second line of text

                 f"\tThe area of the circle of Radius '{str(radius)}'" # Radius
                 f" \tis {str(round(circle_area,2))}"
                 f" Metres Squared\n"

                 # create the third line of text
                 f"\tThe volume of the tank of Height '{str(height)}'" # Height
                 f" \tis {str(round(cylinder_vol,2))}"
                 f" Metres Cubic\n"
                 ) # End of string_format

print(string_format)



