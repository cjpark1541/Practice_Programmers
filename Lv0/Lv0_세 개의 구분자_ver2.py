def solution(my_str):
    list_result=[]; addon=''
    for i in my_str:
        if i=='a'or'b'or'c': list_result.append(addon)
        else: addon=addon+i
    return list_result.append(addon)
    
my_str='baconlettucetomato'
list_result=[]; addon=''
for i in my_str:
    if i=='a'or'b'or'c': 
        list_result.append(addon)
    else:
        addon=addon+str(i)
        print(addon)

print(solution(list_result))