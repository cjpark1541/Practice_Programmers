from functools import reduce
def multiply(list): 
    multiply_value=reduce(lambda x,y:x*y,list)
    return multiply_value   #함수 list 내 곱셈 정의

list_dice=list(input().split())
list_counter=[] #곱셈 list 및 입력 정의

for i in list_dice: counter=list_dice.count(i); list_counter.append(counter)    #element의 반복 확인
k=int(max(list_counter)); print(k)

score_list=[]
for i in range(1,k+1): 
    score_sum=0
    for j in list_dice: 
        score_sum=int(j)**i+score_sum   #각 element의 제곱수들의 list 생성
    score_list.append(score_sum)

print(multiply(score_list)) #곱셈 이용