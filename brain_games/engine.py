import prompt
ROUND_COUNT = 3


def welcome():
    name = prompt.string("May ask you name? ")
    print('Hello,', name)
    return name


def ask_question(question):
    print('Question: ' + question)
    return prompt.string('Your answer: ')


def game(name, game_name, first_string):
    print(first_string)
    i = 0
    while i <= ROUND_COUNT - 1:
        result_game = game_name()
        answer = ask_question(result_game[0])
        if answer == result_game[1]:
            print('Correct')
            i += 1
        else:
            print("'" + answer + "'" + " is wrong answer "
                  ";(. Correct answer was '" + result_game[1] + "'.")
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + "!")
