"""
Credits: Mario Corchero - Exceptional Exceptions Talk @ EuroPython 2019
"""


def main_return():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4


if __name__ == "__main__":
    print(main_return())
