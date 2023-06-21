def solution(arr):
    i=0
    while len(arr)>2**i: i=i+1
    times=2**i-len(arr)
    for i in range(times):
        arr.append(0)
    return(arr)

arr=list(input('input list:').split())
print(solution(arr))
