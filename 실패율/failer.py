N = 5
stages = [2,1,2,6,2,4,3,3]


def solution(N, stages):
    answer = []
    people = len(stages)
    fail = []


#각 스테이지별 실패율 계산을 위해 반복문 작성    
#각 스테이지 끝나면 count 정보 0으로 초기화
    for i in range(1, N+1):
        count = 0
# 스테이지 중 사람 수만큼 반복하여 fail 리스트에 입력
        for j in range(len(stages)):
            if stages[j] == i:
                count += 1
        if count == 0:
            fail.append(0)
#카운트이후 최종 사람수와 나눈호 카운터 숫자만큼 뺄셈 진행
        else:
            fail.append(count/people)
        people = people-count
    
    a = sorted(fail,reverse=True)
    
# a 만큼 다시 반복 해서 
    for q in range(len(a)):
        answer.append(fail.index(a[q])+1)
        fail[fail.index(a[q])]=2
    
    return answer
solution(N, stages)