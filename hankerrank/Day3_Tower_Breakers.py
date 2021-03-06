def towerBreakers(n, m):
    if m == 1:
        return(2)
    if n % 2 == 0:
        return(2)
    return(1)
'''
Consider the solution for the case n=2k, divide the row of towers into two halfs, one half comprising of rows 1 to k and other half for rows k+1 to 2k. Now no matter what move player 1 plays , player 2 replicates it for the mirror image of that tower in the second half. Note that the board will look exactly symmetrical after player 2 has played, throughout the game, consider that only two moves are remaining, then due to the way player 2 played, there must be one move each in each half, player 1 plays something, player 2 does it in the other half and wins.

For n is odd, player 1 realises the above and instantly reduces the last tower to 1, hence no more moves can be done on it, now the situation is identical to n=even, but player 2 plays first and loses.

This assumes that there are moves remaining at the beginning i.e. m!=1; but if m==1 then obviously player 1 will lose.
'''
