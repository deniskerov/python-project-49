from random import randint
import math


def gcd_game():
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    random_string = str(random_int_a) + ' ' + str(random_int_b)
    result = math.gcd(random_int_a, random_int_b)
    return [random_string, str(result)]
