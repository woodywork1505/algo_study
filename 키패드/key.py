numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"


def solution(numbers, hand):
    # answer = ''
    answer = []
    for i in numbers:
        if i == 1:
            answer += "L"
        elif i == 4:    
            answer += "L"
        elif i == 7:    
            answer += "L"
        
        elif i == 3:
            answer += "R"
        elif i == 6:
            answer += "R"
        elif i == 9:
            answer += "R"


        else :
            if hand == 'right':
                answer += "R"
            else:
                answer += "L"
        
    
    
    print(answer)
    return answer

solution(numbers, hand)