# survey = {"RT":0, "TR":0, "FC":0, "CF":0, "MJ":0, "JM":0, "AN":0, "NA":0}
# survey = "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"
# survey = "R", "T", "F", "C", "M", "J", "A", "N"
survey = {"R":0, "T":0, "F":0, "C":0, "M":0, "J":0, "A":0, "N":0}
choices = [3,3,3,3,3,3,3,3]


# def score(survey, choices):
#     # for choice in choices:
#         cnt = 0
#         survey = ["R", "T", "F", "C", "M", "J", "A", "N"]

#         if choices > 4 :
#             s = survey.get(cnt) 
#             s.update(s = choices)
#             cnt += 1
#             # survey[1] == choice
#         elif choices < 4 :
#             s = survey[cnt]            
#             s = choices
#             # s = survey[cnt] 
#             # s.update(s = choices)
#             # survey[0] == choice
#             cnt += 1

#         else : 
#             return
    


# def solution(survey, choices):
#     answer = ''        
    
#     for i in range(len(choices)):
#         cnt = 0 
#         score(survey.get(i), choices[i])
#         cnt = cnt+1

#         if score[0] >= score[1]:
#             answer = score[0]
#         else : 
#             answer = score[1]
            
#         if score[2] >= score[3]:
#             answer = score[2]
#         else : 
#             answer = score[3]    
        
#         if score[4] >= score[5]:
#             answer = score[4]
#         else : 
#             answer = score[5]   
            
#         if score[6] >= score[7]:
#             answer = score[6]
#         else : 
#             answer = score[7]
            
#         if i == 4:
#             i.sort()    
    


    # if i[cnt] == i[cnt+1]:
    #     k = i.sort(i[cnt], i[cnt+1])
    #     print(k)
    # if i[cnt] > i[cnt+1]:
    #     k =i[cnt]
    # else :
    #     k = i[cnt+1]
    #     return k
    # answer = k
    # return answer

def solution(survey, choices):
    choices = [3,3,3,3,3,3,3,3]
    answer = ''
    sur = ["R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 ]
    
    # for i in survey:
    #     for j in choices:
    for key,value in survey.items():
        cnt = 0
        value = choices[cnt]
        if value>4:
            key.update(key = value)
            
            # sur.get(j) == j
        elif value<4:
            key[key].update(key = value)
        
        else:
            return

        newKey = []
        if key[0] >= key[1]:
            newKey[0].add()
        else : 
            newKey[1]
            
        if key[2] >= key[3]:
            newKey[2]
        else : 
            newKey[3]
        
        if key[4] >= key[5]:
            newKey[3]
        else : 
            newKey(5)   
            
        if survey.get(6) >=  survey.get(7):
            newKey(6)
        else : 
            newKey(7)
        
        
        
        answer = newKey    
        # if i == 4:
        #     newKey = i.sort()         
        
        # if survey.get(0) >= survey.get(1):
        #     answer = survey.get(0)
        # else : 
        #     answer = survey.get(1)
            
        # if survey.get(2) >= survey.get(3):
        #     answer = survey.get(2)
        # else : 
        #     answer = survey.get(3)
        
        # if survey.get(4) >= survey.get(5):
        #     answer = survey.get(4)
        # else : 
        #     answer = survey.get(5)   
            
        # if survey.get(6) >=  survey.get(7):
        #     answer = survey.get(6)
        # else : 
        #     answer = survey.get(7)
            
        # if i == 4:
        #     answer = i.sort()         
            
    
solution(survey, choices)