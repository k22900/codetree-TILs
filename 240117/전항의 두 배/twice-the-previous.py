num_list=list(map(int,input().split()))
for i in range(2,10):
    res=num_list[i-1]+(num_list[i-2]*2)
    num_list.append(res)
for i in range(len(num_list)):
    print(num_list[i],end=" ")