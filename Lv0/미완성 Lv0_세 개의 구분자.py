myStr="cabab"
my_list=myStr.split('a')

list_all=[]
for i in my_list:
    new_list=i.split('b')
    list_all.extend(new_list)

list_all2=[]
for j in list_all:
    new_list2=j.split('c')
    list_all2.extend(new_list2)

result=list(filter(None, list_all2))
if len(result)==0: result.append('EMPTY')
print(result)