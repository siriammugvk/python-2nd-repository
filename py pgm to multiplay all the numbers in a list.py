def multiplayList(myList):
    result=1
    for x in myList:
        result=result*x
    return result
list1=[1,2,3]
list2=[3,2,4]
print(multiplayList(list1))
print(multiplayList(list2))