num=int(input())
cnt_five=0
res=0
while True:
    if cnt_five==2:
        break
    res+=num
    print(res,end=" ")
    if res%5==0:
        cnt_five+=1