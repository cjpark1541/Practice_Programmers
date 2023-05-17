def solution(num,divid):
    i1=0; i2=''
    for i in num:
        i1=int(i)+i1; i2=i2+str(i)
    print('i1=',i1,'\n','i2=',i2)
    i1=int(i1)%divid; i2=int(i2)%divid
    return i1,i2

num_input=input('입력(숫자만): ')
n=int(input('나누는 수: '))
ia,ib=solution(num_input,n)
print(ia,ib)