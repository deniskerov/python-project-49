from random import randint


def progression_game():
    random_progression_len = randint(7, 12)
    progression = []
    random_first_num = randint(1, 12)
    random_multiplex = randint(2, 10)
    progression.append(str(random_first_num))
    i = 1
    while i < random_progression_len:
        progression.append(str(int(progression[i - 1]) + random_multiplex))
        i += 1
    random_count = randint(1, random_progression_len - 1)
    result = int(progression[random_count])
    random_string = ' '.join(progression)
    return [random_string.replace(str(result), '..', 1), str(result)]
