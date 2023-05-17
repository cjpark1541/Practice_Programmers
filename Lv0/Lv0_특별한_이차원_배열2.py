arr=list(input().split(','))
print(arr)
n=len(arr)
print(n)
for i in range(n):
    for j in range(n):
        if arr[int(j)][int(i)]==arr[int(i)][int(j)]:
            print('i=',i,'j=',j,arr[int(j)][int(i)],arr[int(i)][int(j)],'같다')
        else: 
            value=0; print('i=',i,'j=',j,arr[int(j)][int(i)],arr[int(i)][int(j)],'다르다')

print(value)