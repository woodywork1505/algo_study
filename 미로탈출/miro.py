#최단경로를 찾기위해 bfs로 푼다
#시작점부터 L까지 BFS탐색
#경로의 길이 저장
#L부터 E까지 BFS탐색
#최종 경로 반환

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

# deque 라이브러리 불러오기
from collections import deque

def solution(maps):
    
    rows,cols = len(maps), len(maps[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    start_r, start_c = start
    queue = collections.deque()
    queue.append((start_r, start_c, 0))

    r,c,distance = 0,0,0
    
    

    answer = 0
    return answer
