#기본 로직
co = int(input())
co_list = []

def opti():
    cnt = 1
    for x in range(co):
        co_in = input()
        co_in = co_in.split()
        co_list.append(co_in)
        
    ind = int(co_list[0][1])
    ind += 1

    for i in range(1,co):
        if int(co_list[i][0]) >= ind:
            cnt += 1
            print(cnt)
            ind = int(co_list[i][1])
            ind += 1
    
    
    return cnt

    
#print(co_list)
print(opti())

# sorted로 앞/뒤 정렬을 하는 이유
# 이미 뒤로 오름차순이 되어있는 입력값이지만 앞뒤가 같거나 하는 반례가 나타날 수도 있기 때문이다.