num=map(int,input().split())
# num_list=[]
num_list=list(map(int,input().split()))
num_list2=[]
for i in num_list:
    if i%2==0:
        num_list2.append(i)
for i in num_list2:
    print(i)        


# print(num_list)