# I need a wristband. Help me in identifying an actual wristband.
# A wristband can have 4 patterns:
# horizontal: each item in a row is identical.
# vertical: each item in each column is identical.
# diagonal left: each item is identical to the one on it's upper left or bottom right.
# diagonal right: each item is identical to the one on it's upper right or bottom left.
# Write a function that returns True if the section can be correctly classified into one of the 4 types, and False otherwise.

def is_wristband(section):
    if horizontal(section):
        return True
    if vertical(section):
        return True
    if diagonal_left(section):
        return True
    if diagonal_right(section):
        return True
    return False


def horizontal(section):
    for row in section:
        if len(set(row)) != 1:
            return False
    return True


def vertical(section):
    for col in zip(*section):
        if len(set(col)) != 1:
            return False
    return True


def diagonal_left(section):
    diagonal = [section[i][i] for i in range(min(len(section), len(section[0])))]
    if len(set(diagonal)) != 1:
        return False
    return True


def diagonal_right(section):
    diagonal = [section[i][len(section[0]) - i - 1] for i in range(min(len(section), len(section[0])))]
    if len(set(diagonal)) != 1:
        return False
    return True


section1 = [["A", "A"], ["B", "B"], ["C", "C"]]
print(is_wristband(section1))
section2 = [["A", "B"], ["A", "B"], ["A", "B"]]
print(is_wristband(section2))
section3 = [["A", "B", "C"], ["C", "A", "B"], ["B", "C", "A"], ["A", "B", "C"]]
print(is_wristband(section3))
section4 = [["A", "B", "C"], ["B", "C", "A"], ["C", "A", "B"], ["A", "B", "A"]]
print(is_wristband(section4))
