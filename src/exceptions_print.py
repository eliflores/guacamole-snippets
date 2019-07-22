"""
Credits: Mario Corchero - Exceptional Exceptions Talk @ EuroPython 2019
"""


def main_print():
    try:
        print(1)
    except:
        print(2)
    else:
        print(3)
    finally:
        print(4)


if __name__ == "__main__":
    main_print()
