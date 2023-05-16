while 1:
    letter,n=input().split(); letter=str(letter); n=int(n)
    if 1<len(letter)<10:
        for i in range(n):
            print(letter)
        break