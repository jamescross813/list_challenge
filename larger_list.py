#Write your function here
def larger_list(lst1, lst2):
    lst1_length=len(lst1)
    lst2_length=len(lst2)
    if(lst1_length>lst2_length):
        return lst1[-1]
    elif(lst2_length>lst1_length):
        return lst2[-1]
    else:
        return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))