#Write your function here
def every_three_nums(start):
    numlst =[]
    if start > 100:
        return numlst
    i = start
    while i <= 100:
        numlst.append(i)
        i += 3
    return numlst
#Uncomment the line below when your function is done
print(every_three_nums(91))

