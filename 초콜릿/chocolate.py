N = 10
M = 4

def solution(N, M):
    # Implement your solution here
    
    while M != 0:
        N, M = M, N%M
        
        if M == 0:
            i = N
        
    answer = N // i
    
    print(answer)
    return answer

solution(N, M)

