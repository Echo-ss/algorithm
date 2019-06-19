#기본 로직
b = int(input())

def coin():
    result = 0
    c = 1000 - b
    
    result += int(c / 500)
    c %= 500
    result += int(c / 100)
    c %= 100
    result += int(c / 50)
    c %= 50
    result += int(c / 10)
    c %= 10
    result += int(c / 5)
    c %= 5
    result += int(c / 1)
    
    return result

print(coin())

#숏코딩
b = int(input())

def coin():
    result = 0
    c = 1000 - b
    c_list = [500, 100, 50, 10, 5, 1]
    
    for x in c_list:
        result += int(c / x)
        c %= x
    
    return result

print(coin())