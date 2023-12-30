num_list=list(map(int,input().split()))

math_sum=[]
for i in num_list:
    if i>=250:
        break
    else:
        math_sum.append(i)
res=sum(math_sum)
avr=res/len(math_sum)
print(res,"%.1f" %(avr))