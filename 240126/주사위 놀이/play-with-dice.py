num_list=list(map(int,input().split()))
num_list.sort()
# n이라는 함수를 0으로 초기화후 1~6까지 가는 for문을작성한뒤 n~10까지 가는 for문을 그안에 작성
# i!=num_list[j]일때 break를사용하여 끝낸다 끝낼때 그동안 나온 횟수를 출력한다
cnt=0
n=0
for i in range(1,7):
    for j in range(n,10):
        if num_list[j]==i:
            cnt+=1
        else:
            n=j
            break
    print(f"{i} - {cnt}")
    cnt=0