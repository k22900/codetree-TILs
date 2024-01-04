num_list=list(map(int,input().split()))
sum_list=[]
for i in num_list:
    if i==0:
        break
    else:
        sum_list.append(i)
sum_list.reverse()
res=0
for i in range(3):
    res+=sum_list[i]
print(res)