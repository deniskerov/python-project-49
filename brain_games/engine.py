import prompt
ROUND_COUNT = 3


def run(game_name, first_answer):
    name = prompt.string("May ask you name? ")
    print('Hello,', name)
    print(first_answer)
    i = 0
    while i <= ROUND_COUNT - 1:
        result_game = game_name()
        print('Question: ' + result_game[0])
        answer = prompt.string('Your answer: ')
        if answer == result_game[1]:
            print('Correct')
            i += 1
        else:
            print("'" + answer + "'" + " is wrong answer "
                  ";(. Correct answer was '" + result_game[1] + "'.")
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + "!")
