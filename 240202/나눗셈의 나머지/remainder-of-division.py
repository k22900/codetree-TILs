a,b=map(int,input().split())

res=0
rem=[0]*b
while True:
    if a<=1:
        break
    res=a//b
    rem[a%b]+=1
    a=res
# print(rem)
sum=0
for e in rem:
    sum+=e*e
print(sum)