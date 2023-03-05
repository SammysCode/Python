# Samantha Bergdahl
def triangleSides(side1, side2, side3):

    if (side1 == side2 == side3):
        return "The triangle is equilateral"
    elif (side1 == side2 != side3 or side1 != side2 == side3 or side1 == side3 != side2):
        return "The triangle is isosceles"
    else:
        return "The triangle is irregular"
