def solution(emergency):
    priority_list=[]
    emergency=list(map(int,emergency))
    new_emergency_list=sorted(emergency,reverse=True)
    for i in emergency:
        priority=new_emergency_list.index(i)+1
        priority_list.append(priority)
    return(priority_list)

emergency=input('응급도 숫자:').split()
print(solution(emergency))