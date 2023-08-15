#누적 주차 시간 계산, 번호 순서대로 요금계산 후 배열 적립
#출차 기록없는 경우 요금계산 주의
#한차량이 여러번에 걸쳐 입 출차 반복 가능

# 입력값 -> [시간 차량번호 출입여부]
# 차량 번호가 같으면 입 출 -> 출차내역 없으면 23:59출차로 간주
# 기본요금  + [(총시간  - 기본시간)/단위시간] * 단위 요금  
# fees -> 기본 시간, 기본 요금, 단위, 단위 요금
# result [14600, 34400, 5000]

#ceil 은 소수점 아래 숫자가 있으면 소수점 아래 전부 버린후 정수부수에 1 더함 -> 올림

import math

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]


def solution(fees, records):
    in_ = dict()
    fee = dict()
    for x in records:
        a,b,c = x.split()
        h,m = a.split(':')
        time = int(h)*60 + int(m)
        if c == 'IN':
            in_[b] = time
        else:
            fee[b] = fee.get(b,0) + (time - in_[b])
            del in_[b]
    for x in in_:
        fee[x] = fee.get(x,0) + 23*60+59 - in_[x]
    answer = []
    for x, y in sorted(fee.items()):
        if y>fees[0]:
            answer.append(fees[1] + math.ceil((y-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
    return answer

solution(fees, records)