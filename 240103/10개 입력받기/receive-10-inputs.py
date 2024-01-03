num_list=list(map(int,input().split()))
res_list=[]
for i in num_list:
    if i==0:
        break
    else:
        res_list.append(i)
        # print(res_list)
res=sum(res_list)
# print(res)
ans=res/len(res_list)
print(res,"%.1f"%(ans))