list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]
def PosiNum(lists):
    Posilists = []
    for i in lists:
        if i>=0:
            Posilists.append(i)
    return Posilists
            
    
    
Posilist1=PosiNum(list1)
Posilist2=PosiNum(list2)
print(Posilist1)
print(Posilist2)
