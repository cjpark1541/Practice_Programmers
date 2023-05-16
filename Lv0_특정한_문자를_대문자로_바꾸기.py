my_string=str(input()); alp=str(input())
alp2=my_string[my_string.find(alp)].upper()
my_string=my_string.replace(alp,alp2)
print(my_string)