#Write your function here
def middle_element(lst):
    if len(lst)%2==0:
        mid = int(len(lst)/2-1)
        sum = lst[mid] + lst[mid+1]
        return sum/2
    else:
        mid = int(len(lst)/2)
        return lst[mid]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))