num_list=list(input().split())
i_odd='0'; i_even='0'
for i in num_list:
    if int(i)%2==0: i_odd=i_odd+i
    else: i_even=i_even+i
print(int(i_odd)+int(i_even))