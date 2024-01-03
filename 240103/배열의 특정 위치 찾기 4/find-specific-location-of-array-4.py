num_list=list(map(int,input().split()))
res_list=[]
for i in num_list:
    if i==0:
        break
    else:
        res_list.append(i)
        # print(res_list)
res=[]
for i in res_list:
    if i%2==0:
        res.append(i)
ans=sum(res)
print(len(res),ans)