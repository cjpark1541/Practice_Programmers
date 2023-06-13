def solution(my_string,indices):
    new_string=''
    for i in range(len(my_string)):
        if not i in indices: new_string=new_string+my_string[i]
    return new_string

my_string="apporoograpemmemprs"
indices=[1, 16, 6, 15, 0, 10, 11, 3]
print(solution(my_string,indices))