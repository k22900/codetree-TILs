stu_point=list(map(int,input().split()))
test_list=[0]*11
res=0
for i in stu_point:
    if i==0:
        break
    res=i//10
    test_list[res]+=1
    # print(est_list)
val=0
for i in range(10,0,-1):
    val=10*i
    print(f"{val} - {test_list[i]}")