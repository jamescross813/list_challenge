#Write your function here 
def double_index(lst, index):
    if(index>= len(lst)):
        return lst
    else:
        newlst = lst[0:index]
        newlst.append(lst[index]*2)
        newlst = newlst + lst[index+1:]
    return newlst
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))