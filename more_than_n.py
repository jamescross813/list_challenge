#Write your function here
def more_than_n(lst, item, n):
    lengthlst= len(lst)
    x=0
    sum =0
    for x in lst:
        if x>lengthlst-1:
            break
        if x==item:
            sum+=1
        x+=1  
    if sum > n:
        return True
    else:
        return False

#Uncomment the line below when your function is done
print(more_than_n([2, 3, 4], 2, 0)) 