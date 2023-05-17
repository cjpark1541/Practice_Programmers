arr=[]; n=int(input('matrix size: '))
for i in range(n):
    input_list=list(input().split())
    arr.append(input_list)

print('array=',arr,'\n','array number=',len(arr))
for i in range(n):
    for j in range(n):
        if arr[int(j)][int(i)]==arr[int(i)][int(j)]: value=1
        else: value=0; break

print('value='value)