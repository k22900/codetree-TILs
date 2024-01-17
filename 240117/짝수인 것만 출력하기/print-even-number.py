num=map(int,input().split())
# num_list=[]
num_list=list(map(int,input().split()))
ans_list=[]
for i in num_list:
    if i%2==0:
        ans_list.append(i)
for i in ans_list:
    print(i,end=" ")        


# print(num_list)