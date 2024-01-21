n=int(input())
num_list=list(map(int,input().split()))
num_list.sort()
# 1이상 9이하의 맞는 각각의 cnt를 선언 후 조건을 세운 뒤에 조건이맞을때 마다 그수의cnt를 올려준 
# num_list를 정렬한뒤 cnt를 1개 선언후 2중for문을 세운다(첫번째는 1부터9까지의수 두번째는 인댁스확인)
# 두번째for문이 끝날때마다 갯수를 출력한뒤 0으로 초기화 
cnt=0
for i in range(1,10):
    for j in range(len(num_list)):
        if num_list[j]==i:
            cnt+=1
    print(cnt)
    cnt=0