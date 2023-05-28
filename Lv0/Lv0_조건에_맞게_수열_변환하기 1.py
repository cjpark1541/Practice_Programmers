list_in=list(input('형식: 1 2 3 4 5\n숫자:').split())
list_out=[]
for i in list_in:
    i=int(i)
    if i>=50 and i%2==0: i=i/2; list_out.append(i)
    elif i<50 and i%2==1: i=i*2; list_out.append(i)
    else: list_out.append(i)
print(*list_out)