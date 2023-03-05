import BirthDateVarification

# Samantha Bergdahl


def main():

    age = abs(int(input("How old are you? ")))

    result = BirthDateVarification.whatAge(age)
    print(result)


if __name__ == "__main__":
    main()
