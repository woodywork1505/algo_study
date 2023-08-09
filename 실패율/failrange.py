#문제는 실패율이 높은 단계를 내림차순으로 정렬
#입력값 개수만큼 도전인원 / 각 스테이지 별 실패율 계산
#N은 스테이지수 해당 스테이지 위에 숫자면 이미 클리어한 상태

#각 스테이지별 실패율
#실패율 순으로 내림차순 정렬
from collections import Counter

N = 5
stages = [2,1,2,6,2,4,3,3]


def solution(N, stages):
    answer = []
    fail = []
    
    counter = Counter(stages)
    # stages_fail = [x for k, x in enumerate(stages) if k != stages.index(x)]
    print(counter[2])
    for i in range(1, N+1):
        # if counter.get(i) == i:
        # if counter[i] == i:
        if counter[i] == None:
            pass
        else:    
            a = counter.get(i)/N
            fail.append(a)
            
        fail.sort()
        
        answer = fail
        
        # for j in stages_fail:
        #     if j <= N:
        #         fail += j
        #     elif j > N:
        #         stages_fail.pop(j)
        print(answer)
        
    return answer

solution(N, stages)