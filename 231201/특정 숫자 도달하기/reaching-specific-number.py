L1=list(map(int,input().split()))
set=0
res=0
AVR=0
# set=L1에서250이상이 처음으로 있는 인덱스값
# res=합계
# AVR=평균
for i in range(10):
    if L1[i]>=250:
        set=i
        break
# print(set)
for i in range(set):
    res+=L1[i]
    # print(res)
AVR=res/set
print(res,AVR)