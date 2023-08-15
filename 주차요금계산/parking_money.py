# 입력값 -> [시간 차량번호 출입여부]
# 차량 번호가 같으면 입 출 -> 출차내역 없으면 23:59출차로 간주
# 기본요금  + [(총시간  - 기본시간)/단위시간] * 단위 요금  
# fees -> 기본 시간, 기본 요금, 단위, 단위 요금
# result [14600, 34400, 5000]

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

def solution(fees, records):
    answer = []
    in_and_out = []

# 입력된 순서대로 시 분 차량번호 등록
    for i in range(len(records)):
        hour = int(records[i][1])
        min = int(records[i][3:5])
        num = records[i][6:10]
        money = []
        
        if records[i][11:13] == 'IN':
            in_and_out = [hour, min, num]
# 기본요금  + [(총시간  - 기본시간)/단위시간] * 단위 요금  
            
        if records[i][11:13] == 'OUT':
            if records[i][11:13] == in_and_out[2]:
                time = hour*60 + min
                money = fees[1] + (((fees[0]-time)/fees[2])*fees[3]) 
                if time <= records[0]:
                    money == 0
        
        answer = money
    print(money)
    return answer

solution(fees, records)