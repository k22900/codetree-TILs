n,m=map(int,input().split())
numbers=list(map(int,input().split()))
cnt=0
for val in numbers:
    if val==m:
        cnt+=1
print(cnt)