num_list=list(map(int,input().split()))

ans_list=[]
for i in num_list:
    if i==0:
        break
    else:
        ans_list.append(i)
        # print(ans_list)
ans_list.reverse()
print(*ans_list)