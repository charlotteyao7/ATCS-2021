#Make a list that includes 3 or 4 games that you like to play.
#Print a statement that tells the user what games you like.
#Ask the user to tell you a game they like, and store the game in a variable such as new_game.
#Add the user's game to your list.
#Print a new statement that lists all of the games that we like to play (we means you and your user).

games = ['Clue', 'Monopoly', 'Scrabble', 'Life']
print('I like Clue, Monopoly, Scrabble, and Life')
new_game = input('What is one game that you like?')
games.append(new_game)
print('We like...')
print(games)