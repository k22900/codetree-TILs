num_list=list(map(int,input().split()))
ten_list=[0]*9
for i in num_list:
    if i==0:
        break
    if i>=10:
        ten_list[(i//10)-1]+=1
for i in range(9):
    print(f"{i+1} - {ten_list[i]}")