def multiply(n):
    multi=1
    for i in range(1,n+1):
        multi=multi*i
    return multi

def solution(balls, Share):
    ways=multiply(balls)/((multiply(balls-share))*multiply(share))
    return ways

balls=5; #int(input('공의 개수:'));
share=3; #int(input('share의 개수:'));
print(solution(balls,share))