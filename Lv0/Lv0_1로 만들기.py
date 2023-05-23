def solution(num_list):
    times=0
    for i in num_list:
        n=0
        while i!=1:
           if i%2==1: i=(i-1)/2
           else: i=i/2
           n=n+1
        times=times+n
    return times

num_list=list(map(int,list(input().split())))
print(solution(num_list))
