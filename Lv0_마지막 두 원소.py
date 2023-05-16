def solution(list_A):
    i=int(len(list_A))
    if int(list_A[i-2])<int(list_A[i-1]):
        Addon=int(list_A[i-1])-int(list_A[i-2]); list_A.append(Addon)
    else:
        Addon=int(list_A[i-1])*2; list_A.append(Addon)
    return list_A

list_input=list(input().split())
print(solution(list_input))