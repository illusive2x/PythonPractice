def invert(list):
    for number in list:
        list[number] *= -1
    return list

list = [1,2,3,4,5]
list2 =[-5,-4,-3,-2,-1]

invert(list)
invert(list2)

print(list)
print(list2)
