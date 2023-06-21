def solution(bin1,bin2):
    bin_addon=bin(int(bin1,2)+int(bin2,2))
    return bin_addon.replace('0b','')

bin1="10"; bin2="11"
print(solution(bin1,bin2))
