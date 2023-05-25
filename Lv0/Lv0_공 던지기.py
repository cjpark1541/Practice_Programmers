def solution(numbers,k):
    index=2*(k-1)
    while len(numbers)<index: numbers.extend(numbers)
    return numbers[index]

num_list=list(input('list 입력').split())
num=int(input('던지는 수:'))
print(solution(num_list,num))
