def solution(date1,date2):
    if date1[0]<date2[0]: return 1
    if date1[0]>date2[0]: return 0
    else:
        if date1[1]<date2[1]: return 1
        elif date1[1]>date2[1]: return 0
        else:
            if date1[2]<date2[2]: return 1
            else: return 0

new_list=[]
date1=list(input('date1:').split())
date2=list(input('date2:').split())
print(solution(date1,date2))

