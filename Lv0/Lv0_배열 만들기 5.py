def solution(intStrs,k,s,l):
    new_list=[]
for i in intStrs:
    if int(i[s:s+l])>k: new_list.append(int(i[s:s+l]))
print(new_list)

intStrs=["0123456789","9876543210","9999999999999"]
k=50000; s=5; l=5

