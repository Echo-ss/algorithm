#!/usr/bin/env python
# coding: utf-8

# # 백준 온라인 저지 2750번 (정렬)
# 
# #### 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 
# #### 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 
# #### 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# ##### JUPYTER NOTEBOOK에서는 sys.stdin.readline()이 되질 않는다. input()으로만 사용

# In[2]:


#import sys
sort_list = []
temp = 0

#num_line = int(sys.stdin.readline())
print("입력값 :")
num_line = int(input())

for i in range(num_line):
#    sort_list.append(int(sys.stdin.readline()))
    sort_list.append(int(input()))
    for x in range(i, 0, -1):
        if i == 0:
            continue
        elif sort_list[x-1] > sort_list[x]:
            temp = sort_list[x-1]
            sort_list[x-1] = sort_list[x]
            sort_list[x] = temp
        else:
            continue

print("출력값 :")
for i in range(num_line):
    print(sort_list[i])


# In[ ]:




