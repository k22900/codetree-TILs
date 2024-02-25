N=int(input())
Ns=list(map(int,input().split()))
Ns.sort(reverse=True)
for i in range(2):
    ans=Ns[i]
    ans=int(ans)
    print(ans,end=" ")