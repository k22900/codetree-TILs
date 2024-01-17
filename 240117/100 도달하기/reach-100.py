n=list(map(int,input().split()))
cnt=2
res=n[0]
n.append(res)
print(1,res,end=" ")
n[0]=1
    
while True:
    ans=n[cnt-2]+n[cnt-1]
    n.append(ans)
    print(ans,end=" ")
    cnt+=1
    if ans>=100:
        break