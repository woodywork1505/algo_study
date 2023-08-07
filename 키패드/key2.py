# 1. 키패드 생성
# 2. numbers 한개씩 리스트 저장
# 3. 손가락 위치를 저장하는 코드 필요
# 4. 시작은 * 끝은 #
# 5. 위치 고려하여 2580은 왼손 오른손 잡이가 결정하는 구문 추가
# 5. answer += L,R


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

# 키패드 좌표 표시
keypad = {1:[0,0],2:[0,1],3:[0,2],
            4:[1,0],5:[1,1],6:[1,2],
            7:[2,0],8:[2,1],9:[2,2],
            '*':[3,0],0:[3,1],'#':[3,2]}


def solution(numbers, hand):
    start = [3,0]
    finish = [3,2]
    
    answer = []
    
    for i in numbers:
        if i == 1:
            answer += "L"
            start = [0,0]
        elif i == 4:    
            answer += "L"
            start = [1,0]
        elif i == 7:    
            answer += "L"
            start = [2,0]
        
        elif i == 3:
            answer += "R"
            finish = [0,2]
        elif i == 6:
            answer += "R"
            finish = [1,2]
        elif i == 9:
            answer += "R"
            finish = [2,2]


        elif i == 2:
            
            
            
            if hand == 'right':
                answer += "R"
                start 
            else:
                answer += "L"
        
    
    
    print(answer)
    return answer

solution(numbers, hand)