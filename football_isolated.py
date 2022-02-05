def solution(gameMap):
    m = len(gameMap[0])
    cnt = 0
    # Please write your code here.
    def isolate(r,c,gameMap,m):
        if r == 0:
            if c == 0:
                if gameMap[r][c+1] == 'A' or gameMap[r+1][c+1] == 'A' or gameMap[r+1][c] == 'A':
                    return False
            elif c == m - 1:
                if gameMap[r+1][c] == 'A' or gameMap[r+1][c-1] == 'A' or gameMap[r][c-1] == 'A':
                    return False
            else:
                if gameMap[r][c-1] == 'A' or gameMap[r][c+1] == 'A' or \
                gameMap[r+1][c-1] == 'A' or gameMap[r+1][c] == 'A' or gameMap[r+1][c+1] == 'A':
                    return False
        elif r == m - 1:
            if c == 0:
                if gameMap[r][c+1] == 'A' or gameMap[r-1][c+1] == 'A' or gameMap[r-1][c] == 'A':
                    return False
            elif c == m - 1:
                if gameMap[r-1][c] == 'A' or gameMap[r-1][c-1] == 'A' or gameMap[r][c-1] == 'A':
                    return False
            else:
                if gameMap[r][c-1] == 'A' or gameMap[r][c+1] == 'A' or \
                gameMap[r-1][c-1] == 'A' or gameMap[r-1][c] == 'A' or gameMap[r-1][c+1] == 'A':
                    return False
        else:
            if c == 0:
                if gameMap[r-1][c] == 'A' or gameMap[r+1][c] == 'A' or \
                gameMap[r-1][c+1] == 'A' or gameMap[r][c+1] == 'A' or gameMap[r+1][c+1] == 'A':    
                    return False
            elif c == m - 1:
                if gameMap[r-1][c] == 'A' or gameMap[r+1][c] == 'A' or \
                gameMap[r-1][c-1] == 'A' or gameMap[r][c-1] == 'A' or gameMap[r+1][c-1] == 'A':
                    return False
            else:
                if 'A' in gameMap[(r-1):(r+2)][c-1] or 'A' in gameMap[(r-1):(r+2)][c+1] or gameMap[r-1][c] == 'A' or gameMap[r+1][c] == 'A':
                    return False
        return True
    
    for r in range(m):
        for c in range(m):
            if gameMap[r][c] == 'A':
                if isolate(r,c,gameMap,m):
                    cnt += 1
    
    return cnt
