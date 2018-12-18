def getList(num):
    list=[]
    n=1
    while n<=num:
        list.append("num:"+str(n))
        n+=1
    return list

print(getList(5))
        
