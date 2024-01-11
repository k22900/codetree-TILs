arr=list(map(int,input().split()))
for i in range(2,10):
    num=arr[i-2]+arr[i-1]#
    if  num>=10:
        num-=10
    arr.append(num)
for i in range(10):
    print(arr[i],end=" ")