#Write your function here
def append_sum(lst):
    length = len(lst)
    sum = 0
    x=0
    for x in lst:
        sum+=lst[x]
        x+=1
        if x == length:
            break
    
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
