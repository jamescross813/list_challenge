#Write your function here
def more_frequent_item(lst, item1, item2):
    num_itm1 = 0
    num_itm2 = 0
    for x in lst:
        if x==item1:
            num_itm1+=1
        elif x == item2:
            num_itm2+=1
        else:
            break
    
#Uncomment the line below when your function is done
#print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))