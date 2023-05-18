def solution(i,j,k):
    n_list=list(map(str,list(range(int(i),int(j)+1))))
    n_str=''.join(n_list)
    return(list(n_str).count(str(k)))

i,j,k=input('처음시작값,나중값,찾을값:').split(',')
print(solution(i,j,k))
