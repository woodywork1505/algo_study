from collections import defaultdict

survey = ["TR", "RT", "TR"]
choices = [7,1,3]

def solution(survey, choices):
    answer = ''
    
    #알바팻 순서 오름차순 선정리
    sur = [['R','T'], ['C','F'], ['J','M'], ['A','N']]
    #딕셔너리 int기준 생성 값은 0으로 자동 초기화
    default_sur = defaultdict(int)
    
    for i,j in zip(survey, choices):
        if j > 4:
            default_sur[i[1]] += (j-4)
        elif j < 4:
            default_sur[i[0]] += (4-j)
            
    for i in sur:
        #같을 경우를 대비하여 미리 오름차순 정리함
        if default_sur[i[0]] >= default_sur[i[1]]:
            answer += i[0]
        else:
            answer += i[1]

    print(answer)
    return answer

solution(survey, choices)