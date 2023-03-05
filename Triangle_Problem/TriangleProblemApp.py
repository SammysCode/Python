from unittest import result
import TriangleProblem

# Samantha Bergdahl


def main():
    side1 = abs(int(input("Set the length of the first side of the triangle: ")))
    side2 = abs(
        int(input("Set the length of the second side of the triangle: ")))
    side3 = abs(int(input("Set the length of the third side of the triangle: ")))

    result = TriangleProblem.triangleSides(side1, side2, side3)

    print(result)


if __name__ == "__main__":
    main()
