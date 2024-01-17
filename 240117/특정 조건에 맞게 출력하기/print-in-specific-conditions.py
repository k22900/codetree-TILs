num_list=list(map(int,input().split()))
val_list=[]
for i in num_list:
    if i==0:
        break
    else:
        val_list.append(i)
for i in range(len(val_list)):
    if val_list[i]%2==0:
        ans=val_list[i]//2
        print(ans,end=" ")
    else:
        ans=val_list[i]+3
        print(ans,end=" ")