my_string=input('string is:'); new_list=[]
for i in my_string:
    if str(i) not in new_list: new_list.append(str(i))
new_str=''.join(new_list)

print('new string is:',new_str)
