# 1. 키패드 생성
# 2. numbers 한개씩 리스트 저장
# 3. 손가락 위치를 저장하는 코드 필요 or 2580 거리 비교를 미리 해준다.
# 4. 시작은 * 끝은 #
# 5. 위치 고려하여 2580은 왼손 오른손 잡이가 결정하는 구문 추가
# 5. answer += L,R




numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

# 키패드 순서대로 2,5,8,0 간의 거리를 입력
# ex) 1: [2와의 거리, 5와의 거리, 8과의 거리, 0간의 거리]
keypad = {1:[1,2,3,4],2:[0,1,2,3],3:[1,2,3,4],
            4:[2,1,2,3],5:[1,0,1,2],6:[2,1,2,3],
            7:[3,2,1,2],8:[2,1,0,1],9:[3,2,1,2],
            '*':[4,3,2,1],0:[3,2,1,0],'#':[4,3,2,1]}



def solution(numbers, hand):
    start = '*'
    finish = '#'
    current = 0
    
    answer = []
    
    for i in numbers:
        if i == 1:
            answer += "L"
            start = i
        elif i == 4:    
            answer += "L"
            start = i
        elif i == 7:    
            answer += "L"
            start = i
            
        elif i == 3:
            answer += "R"
            finish = i
        elif i == 6:
            answer += "R"
            finish = i
        elif i == 9:
            answer += "R"
            finish = i

        elif i ==2 or i ==5 or i ==8 or i ==0:
            if i == 2:
                current = 0
                
                #거리가 더 길면 반대편 손가락이 가까운것!
                #비교후에 키패드 번호를 저장 => start finish
            
                if keypad[start][current] > keypad[finish][current]:
                    answer += "R"
                    finish = i
                elif keypad[start][current] < keypad[finish][current]:
                    answer += "L"
                    start = i
                else : 
                    if hand == 'right':
                        answer += "R"
                        finish = i
                    else:
                        answer += "L"
                        start = i
                        
            elif i == 5:
                current = 1
                if keypad[start][current] > keypad[finish][current]:
                    answer += "R"
                    finish = i
                elif keypad[start][current] < keypad[finish][current]:
                    answer += "L"
                    start = i
                else : 
                    if hand == 'right':
                        answer += "R"
                        finish = i
                    else:
                        answer += "L"   
                        start = i
                        
            elif i == 8:
                current = 2
                if keypad[start][current] > keypad[finish][current]:
                    answer += "R"
                    finish = i
                elif keypad[start][current] < keypad[finish][current]:
                    answer += "L"
                    start = i
                else : 
                    if hand == 'right':
                        answer += "R"
                        finish = i
                    else:
                        answer += "L"
                        start = i
                        
            elif i == 0:
                current = 3
                if keypad[start][current] > keypad[finish][current]:
                    answer += "R"
                    finish = i
                elif keypad[start][current] < keypad[finish][current]:
                    answer += "L"
                    start = i
                else : 
                    if hand == 'right':
                        answer += "R"
                        finish = i
                    else:
                        answer += "L"
                        start = i
                        
    print(answer)
    return answer

solution(numbers, hand)