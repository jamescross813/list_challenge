#Write your function here
def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# #Write your function here
# def append_sum(lst):
#     length = len(lst)
#     sum = 0
#     x=0
#     for x in lst:
#         sum+=lst[x]
#         x+=1
#         if x == length:
#             break
#     lst.append(sum) 
#     return lst
# #Uncomment the line below when your function is done
# print(append_sum([1, 1, 2]))
