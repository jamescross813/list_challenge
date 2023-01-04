#Write your function here
def more_than_n(lst, item, n):
    lengthlst= len(lst)
    x=0
    for x in lst:

        x+=1
        if x==lengthlst-1:
            break

#Uncomment the line below when your function is done
#print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))