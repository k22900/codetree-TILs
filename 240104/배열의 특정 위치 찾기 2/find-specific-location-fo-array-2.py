num_list=list(map(int,input().split()))
sig_list=[]
dub_list=[]
for i in range(10):
    if i%2==0:
        sig_list.append(num_list[i])
    else:
        dub_list.append(num_list[i])
# print(sig_list,dub_list)
res1=sum(sig_list)
res2=sum(dub_list)
if res1>res2:
    print(res1-res2)
else:
    print(res2-res1)