# 다이나믹 프로그래밍 바텀업
# 꼭대기를 제외한 다음층 부터 최대가 될 수 있게 갱신

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0
    
    #총높이
    for i in range(1, len(triangle)):
    #총 길이
        for j in range(len(triangle[i])):
            
            if j == 0:
                #왼쪽 대각선 위에서 내려옴
                #첫번째 숫자일때 위의 수와 던한값
                triangle[i][j] += triangle[i-1][0]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
            answer = max(triangle[i])    
            # answer = triangle[i][j]
    
    print(answer)
    return answer



solution(triangle)