alpha=str(input()); list_alpha=list(alpha); alpha2=''
while not alpha.isalpha(): alpha=str(input())

for  alpha in list_alpha:
    if alpha.islower(): alpha=alpha.upper();
    else: alpha=alpha.lower()
    alpha2=alpha2+alpha

print(alpha2)