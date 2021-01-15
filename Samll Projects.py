from random import randint
game=randint(0,21)
print('Game:',game)
guess=randint(0,21)
print('Guess:',guess)

if guess>game:
    print('TOO HIGH')
elif guess==game:
    print('LUCKY YOU')
elif guess<game:
    print('TOO LOW\n\n\n')


