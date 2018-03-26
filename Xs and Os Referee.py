def checkio(game_result):
    """
        A game's result is presented as a list of strings,
        where "X" and "O" are players' marks and "." is the empty cell.
        This function determine if the game ends in a win
        or a draw as well as who will be the winner.
    """
    for row in list(game_result):
        if row.count("X") == 3:
            return "X"
        elif row.count("O") == 3:
            return "O"
        else: continue
    rotated = list(zip(*game_result))
    for line in rotated:
        if line.count("X") == 3:
            return "X"
        elif line.count("O") == 3:
            return "O"
        else: continue
    if rotated[0][0] == rotated[1][1] == rotated[2][2] == "X":
        return "X"
    elif rotated[0][0] == rotated[1][1] == rotated[2][2] == "O":
        return "O"
    elif rotated[0][2] == rotated[1][1] == rotated[2][0] == "X":
        return "X"
    elif rotated[0][2] == rotated[1][1] == rotated[2][0] == "O":
        return "O"
    else: return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    game_result = input("Enter a game result as a list of strings: ")
    print(checkio(game_result))

"""
    Good example:
    
    def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
"""