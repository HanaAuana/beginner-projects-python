from random import randint

responses = ['Ask again later',
             'Outlook not good',
             'Definitely',
             'Unlikely',
             'Perhaps',
             'It is certain',
             'Yes',
             'Cannot predict now',
             'Doubtful',
             'Most likely', ]


def get_response():
    choice = randint(0, 9)
    return responses[choice]

while True:
    question = input('Ask a question: ')
    print('Thinking...')
    print(get_response())
    again = input('Do you want to ask again? Type yes to continue: ')
    if again.lower() not in ('yes', 'y', 'continue'):
        break
