n=int(input())

# 소수란 약수가 1과 자기자신만 있는수를 말한다(단 소수!=1)
cnt=0

for i in range(2,n+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        print(i,end=" ")