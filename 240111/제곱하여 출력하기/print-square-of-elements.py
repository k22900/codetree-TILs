num1=int(input())
arr=list(map(int,input().split()))
for i in range(num1):
    arr[i]=arr[i]*arr[i]
    print(arr[i],end=" ")