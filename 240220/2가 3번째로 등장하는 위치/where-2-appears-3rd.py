n=int(input())
# 정수n개를 받는다
# n은 뭐지?
# n은 언제 결정되지?
# n은 현재모르는구나
# 그러면 내가 몇개를 초기화 해야하는지모르는 구나
# 그러면 일단은 한줄로 받아야 하니까 배열로 받아야 겠다
nums=list(map(int,input().split()))
# 내가 뭘했는지 물어보고 
# 내가 뭘했는지 답하고
# 내가 뭘해야되는지 물어보고
# 내가뭘할건지 대답하자
cnt=0
for i in range(n):
    if nums[i]==2:
        cnt+=1
    if cnt==3:
        ans=i+1
        print(ans)
        break