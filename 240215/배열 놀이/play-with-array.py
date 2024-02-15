def findNum(n1):
    for idx,el in enumerate(num):
        if el==n1:
            return idx
    return 0

def nums(n1,n2):
    num_list=[]
    for i in range(n1-1,n2):
        num_list.append(num[i])
    return num_list

n,q=map(int,input().split())#원소가 주어지는지 개수를 알려주는n,질의의 개수를 알리는q
num=list(map(int,input().split()))#n개의 원소를 받는 배열num

for _ in range(q):
    task=list(map(int,input().split()))
    if task[0]==1:#a번쨰 원소출력
        ans=num[task[1]-1]
        print(ans)    
    elif task[0]==2:#a가 몇번째 
        ans=findNum(task[1])
        print(ans+1)
    elif task[0]==3:
        ans=nums(task[1],task[2])
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()