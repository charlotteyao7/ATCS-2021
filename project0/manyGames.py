# Modify Game Preferences so your user can add as many games as they like.

games = ['Clue', 'Monopoly', 'Scrabble', 'Life']
print('I like Clue, Monopoly, Scrabble, and Life')
new_game = ''
while new_game != 'none':
    new_game = input('What are some games that you like? If you have no more games, type "none"')
    games.append(new_game)
print('We like...')
print(games)