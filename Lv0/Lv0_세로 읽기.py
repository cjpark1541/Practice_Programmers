#def solution(my_string,m,c)
my_string='ihrhbakrfpndopljhygc'
m=4; c=2; string_list=[]
for i in range(0,len(my_string),m):
    new_string=my_string[int(i),int(i)+m]
    string_list.append(new_string)
print(string_list)