hum=int(input())
cnt=0
for i in range(hum):
    stu_list=[]
    stu_list=list(map(int,input().split()))
    avr=sum(stu_list)/len(stu_list)
    if avr>=60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)