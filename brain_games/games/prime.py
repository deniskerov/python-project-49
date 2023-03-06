from random import randint
FIRST_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = 0
    for j in range(2, number):
        if (number % j == 0):
            i += 1
    if (i <= 0):
        return True
    else:
        return False


def generate_round():
    random_number = randint(2, 199)
    if is_prime(random_number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return [str(random_number), answer]
