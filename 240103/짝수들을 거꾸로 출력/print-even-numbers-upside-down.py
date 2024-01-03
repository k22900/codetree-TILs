nums=int(input())
num_list=list(map(int,input().split()))
res=[]
for i in num_list:
    if i%2==0:
        res.append(i)
res.reverse()
print(*res)