num_list=list(map(int,input().split()))
dub_list=[]
tre_list=[]
for i in range(10):
    if i%2==1:
        dub_list.append(num_list[i])
    if i%3==2:
        tre_list.append(num_list[i])
# print(tre_list)
res=sum(dub_list)
avr=sum(tre_list)/len(tre_list)
print(res,"%.1f"%(avr))