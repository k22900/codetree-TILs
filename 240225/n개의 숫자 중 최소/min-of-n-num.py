N=int(input())
Ns=list(map(int,input().split()))
N_min=min(Ns)
ans=Ns.count(N_min)
print(N_min,ans)