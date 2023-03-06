from random import randint
FIRST_ANSWER = 'Find the greatest common divisor of given numbers.'


def generate_gcd(int_a, int_b):
    if int_a > int_b:
        smaller_int = int_b
    else:
        smaller_int = int_a
    for i in range(1, smaller_int + 1):
        if ((int_a % i == 0) and (int_b % i == 0)):
            gcd = i
    return gcd


def generate_round():
    random_int_a = randint(1, 100)
    random_int_b = randint(1, 100)
    random_string = str(random_int_a) + ' ' + str(random_int_b)
    result = generate_gcd(random_int_a, random_int_b)
    return [random_string, str(result)]
