import re


def password():
    """Returns the number of possible password combinations"""

    combinations_number = 0

    for number in range(372 ** 2, (809 ** 2) + 1):
        number = str(number)
        if not any(number[i] > number[i + 1] for i in range(5)):
            matches = re.findall("22+|33+|44+|55+|66+|77+|88+|99+", number)
            if len(matches) >= 2:
                combinations_number += 1
    return combinations_number


if __name__ == '__main__':
    print(password())
