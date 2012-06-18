import shelve

"""Write a function (not a class) that takes two arguments, a string player name and an integer score, 
    and keeps a "high score" table in a Python shelve. If the integer argument is higher than the 
    given player's current high score (or if the player has no recorded high score), 
    log the value as this player's new high score. The function should return the player's current high score. """
    
def high_score(player, score):

    shelf = shelve.open('myshelf.shlf')

    if player not in shelf:
        shelf[player] = score
        highscore = score
    elif shelf[player] < score:
        shelf[player] = score
        highscore = score
    else:
        highscore = shelf[player]
        
    shelf.close()

    return highscore