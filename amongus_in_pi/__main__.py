import pathlib
from decimal import getcontext, Decimal
from typing import Iterator


def pi():
    """Compute Pi to the current precision.

    >>> print(pi())
    3.141592653589793238462643383

    Taken from https://docs.python.org/3/library/decimal.html

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision


def find_amonguses_in_num(num_str: str, amongus: str) -> Iterator[int]:
    """
    Yield every index of digit of num where we find the hiding amongus
    :param num_str: integer to search for converted to a string
    :param amongus: string of binary digits representing the amongus
    :return: every index of hiding amonguses
    """
    num_str = "".join(("0" if int(digit_chr) <= 4 else "1" for digit_chr in num_str))

    for i in range(len(num_str)):
        if num_str[i:i + len(amongus)] == amongus:
            yield i


def main():
    """
    BIG_PI_STR holds pi to the 500_000th digit, calculated with:

    >>> getcontext().prec = 500_000
    >>> print(pi())

    It takes a while to run, so it's better to hold the value in a file.
    I manually removed the "3." from the file.
    """

    with open(pathlib.Path(__file__).parent / "bigpi.txt", "r") as file:
        BIG_PI_STR = file.readline()

    amongus_str = """
       ________
    __|  ______|
    |    |_____|
    |__   __   | 
      |__|  |__|
    """
    amongus = [
        0, 1, 1, 1,
        1, 1, 0, 0,
        1, 1, 1, 1,
        0, 1, 0, 1,
    ]
    print(amongus_str)
    amongus = "".join(map(str, amongus))

    for amongus_pos in find_amonguses_in_num(num_str=BIG_PI_STR, amongus=amongus):
        end_pos = amongus_pos+len(amongus)
        print(f"Something sus about digits => {amongus_pos} to {end_pos}")


if __name__ == "__main__":
    main()
