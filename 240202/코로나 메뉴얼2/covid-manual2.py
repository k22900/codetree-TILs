cov_Lv=[0]*4
for i in range(3):
    sym,tem=input().split()
    tem=int(tem)
    if sym=="Y":
        if tem>=37:
            cov_Lv[0]+=1
        else:
            cov_Lv[2]+=1
    else:
        if tem>=37:
            cov_Lv[1]+=1
        else:
            cov_Lv[3]+=1

for i in range(4):
    print(cov_Lv[i],end=" ")

if cov_Lv[0]>=2:
    print("E",end=" ")