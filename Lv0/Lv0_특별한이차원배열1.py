def solution(n):
    list_new=[]
    for i in range(n):
        list_addon=[]
        for j in range(n):
            if i==j: addon=1
            else: addon=0
            list_addon.append(addon)
        list_new.append(list_addon)
    return list_new

n=int(input('숫자 입력:'))
print(solution(n))
