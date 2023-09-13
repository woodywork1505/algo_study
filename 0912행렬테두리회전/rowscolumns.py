rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


def solution(rows, columns, queries):
    answer = 0
    table = []
    
    table = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for i in range(rows):
        for j in range(columns):
            table[i][j] = t
            t += 1                   
        print(table)
    
    for x1, y1, x2, y2 in queries:
        #시작점, 가로 옮길 값
        tmp = table[x1-1][y1-1]
        move = tmp
        
        # 세로 , x축을 고정 하기위해 x축을 반복하여 y를 줄인다
        for k in range(x1 -1, x2 -1):
            row = table[k+1][y1-1]
            table[k][y1-1] = row
            move = min(move, row)
        
        # 하단 가로
        for k in range(y1-1, y2-1):
            col = table[x2-1][k+1]
            table[x2-1][k] = col
            move = min(move, col)
            
        #우측 세로
        for k in range(x2-1, x1-1, -1):
            row = table[k-1][y2 -1]
            table[k][y2-1] = row
            move = min(move, row)
            
        #상단 가로
        for k in range(y2-1, y1-1, -1):
            col = table[x1-1][k-1]
            table[x1-1][k]
            move = min(move, col)
            
        table[x1-1][y1] = tmp
        minin = min(table)
        answer = minin
        
        
    return answer

solution(rows, columns, queries)