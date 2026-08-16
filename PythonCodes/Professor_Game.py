import random


def main():
    level = get_level()

    Corr_Count = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        counter = 0
        while counter != 3:
            result = input((f"{x} + {y} = "))
            try:
                if (x + y) == int(result):
                    Corr_Count += 1
                    break
                else:
                    print("EEE")
                    counter += 1

            except ValueError:
                print("EEE")
                counter += 1

            if counter == 3:
                print(f"{x} + {y} = {x+y}")
                break

    print(f"the number of correct answers out of 10 is {Corr_Count}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
            else:
                raise ValueError()

        except ValueError:
            pass

#This function is used to retrieve the numbers instead of generating the numbers in main.
def generate_integer(level):

    return random.randrange(10*int((10**(level-2))),(10**level))


if __name__ == "__main__":
    main()
