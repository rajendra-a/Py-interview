import random

def read_random(filename):
    lines = open(filename).read().splitlines()
    return random.choice(lines)
