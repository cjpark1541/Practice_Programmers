def solution(arr,queries):
    for i in range(len(queries)):
        i_min=min(queries[i]); i_max=max(queries[i])
        for j in range(i_min,i_max+1):
            arr[j]=int(arr[j])+1
    return arr

arr=list(map(int,list(input('array 입력:').split())))
queries=[]
while input('입력할것인가')!='X':
    new_queries=list(map(int,list(input('query 입력:').split())))
    queries.append(new_queries)

print(solution(arr,queries))