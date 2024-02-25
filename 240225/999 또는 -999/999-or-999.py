nums=list(map(int,input().split()))
res_list=[]
for elm in nums:
    if elm==-999 and elm== 999:
        break
    res_list.append(elm)

res_min=min(res_list)
res_max=max(res_list)
print(res_max,res_min)