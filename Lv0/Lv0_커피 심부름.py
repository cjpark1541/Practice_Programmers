def soluion(order):
    dictionary={
        'iceamericano': '차가운 아메리카노', 'americanoice': '차가운 아메리카노', 
        'hotamericano': '따뜻한 아메리카노', 'americanohot': '따뜻한 아메리카노', 
        'icecafelatte': '차가운 카페 라테', 'cafelatteice': '차가운 카페 라테', 
        'hotcafelatte': '따뜻한 카페 라테', 'cafelattehot': '따뜻한 카페 라테',
        'americano': '아메리카노', 
        'cafelatte': '카페 라테',
        "anything": '아무거나'}
    dictionary2={'차가운 아메리카노':'4500', '따뜻한 아메리카노':'4500', '차가운 카페 라테':'5500','따뜻한 카페 라테':'5000', '아메리카노':'4500', '카페 라테':'5000', '아무거나':'4500'}
    price=0
    for i in order:
        j=dictionary[i]; k=dictionary2[j]; price=price+int(k)
    return price

order=["americanoice", "americano", "iceamericano"]	#list(input('input=').split())
print(soluion(order))