MAX_DIMENSION = 150
MAX_VOLUME = 1_000_000
MAX_MASS = 20


def is_bulky(width, height, length):
    return any(dim >= MAX_DIMENSION for dim in (width, height, length)) or \
       width * height * length >= MAX_VOLUME


def is_heavy(mass):
    return mass >= MAX_MASS


def sort(width, height, length, mass):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
