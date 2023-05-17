def multiple(arr):
    output=1;
    for i in arr: output=output*i
    return output
    
list_n=input().split(); 
if len(list_n)>=11: output=sum(list_n)
else: multiple(list_n);
print(output)