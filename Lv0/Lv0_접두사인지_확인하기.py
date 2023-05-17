string=list(input('my string is:')); prefix=list(input('prefix is:'))
for i in range(len(prefix)-1):
    if string[i]==prefix[i]: output=1
    else: output=0
print(output)