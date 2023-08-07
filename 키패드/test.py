numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

keypad = {1:[1,2,3,4],2:[0,1,2,3],3:[1,2,3,4],
            4:[2,1,2,3],5:[1,0,1,2],6:[2,1,2,3],
            7:[3,2,1,2],8:[2,1,0,1],9:[3,2,1,2],
            '*':[4,3,2,1],0:[3,2,1,0],'#':[3,2,1,0]}



def solution(numbers, hand):
    start = '*'
    finish = '#'
    current = 0
    
    answer = ''
    
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
    return answer
