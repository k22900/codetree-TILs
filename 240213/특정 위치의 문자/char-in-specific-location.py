# def find(txt):
#     for i in text_list:
#         if i==txt:
#             res=text_list.index(i)
#             return(res)
#     return("None")

# def find(txt):
#     for i in range(len(text_list)):
#         if text_list[i]==txt:
#             return(i)
#     return("None")

def find(txt):
    for i,char in enumerate(text_list):
        if char==txt:
            return(i)
    return("None")


text_list=["L","E","B","R","O","S"]
text=input()
ans=find(text)
print(ans)