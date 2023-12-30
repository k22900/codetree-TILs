num=int(input())
num_list=list(map(float,input().split()))

res=sum(num_list)
avr=res/num
if avr>=4.0:
    rak="Perfect"
elif avr>=3.0:
    rak="Good"
else:
    rak="Poor"
print("%.1f" %(avr),rak,sep="\n")