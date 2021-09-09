# PythonList_8-9-21
#Excises 1:
def largestdonate(name, amounts):
    if len(name) == 0 or len(amounts) == 0:
        return None
    maxMonney = amounts[0]
    for i in range(len(amounts)):
        num = amounts[i]
        if maxMonney < amounts[i]:
            maxMoney = amounts[i]
            num1 = name[i]
    print("Nguoi gop so tien nhieu nhat la:", num1)
   
def smallestdonate(name, amounts):
    if len(name) == 0 or len(amounts) == 0:
        return None
    minMonney = amounts[0]
    for i in range(len(amounts)):
        num = amounts[i]
        if minMonney > amounts[i]:
            minMoney = amounts[i]
            num1 = name[i]
    print("Nguoi gop so tien it nhat la:", num1)

def avgdonate(amounts):
    if len(amounts) == 0:
        return 0
    allMoney = 0
    lennum = len(amounts)
    for i in range(lennum):
        num = amounts[i]
        allMoney += num
    avgMoney = allMoney / lennum
    print("Trung binh so tien gop duoc la:", avgMoney)

#Case1:
name = ["Duong", "Mai", "Hoa", "Dao"]
amounts = [109000, 60000, 10000, 1200000]
#Call function:
largestdonate(name, amounts)
smallestdonate(name, amounts)
avgdonate(amounts)

#Case2:
name1 = []
amounts1 = []
#Call function:
largestdonate(name1, amounts1) #List name và amounts đều rỗng
smallestdonate(name1, amounts) #List name rỗng nhưng list amounts k rỗng
avgdonate(amounts1) #List amounts rỗng

#Case3:
name2 = []
amounts2 = [120, 100, 5000, 6500]
#Call function
largestdonate(name2, amounts2) #List name rỗng nhưng list amounts k rỗng
smallestdonate(name, amounts1) #List name k rỗng nhưng list amounts rỗng
avgdonate(amounts1) #List amounts rỗng
avgdonate(amounts2) #List amounts k rỗng

#Excises 2:
name = ["Duong", "Mai", "Hoa", "Dao"]
amounts = [109000, 60000, 10000, 1200000]

#Case use "in":
def look(name, amounts, name1, money):
    if name1 in name and money in amounts:
        return True
    else:
        return False

#Call function:
ex1 = look(name, amounts, "Mai", 60000)  
print(ex1) #Kết quả ra True
ex2 = look(name, amounts, "Duong", 100000) 
print(ex2) #Kết quả ra False: có tên nhưng k đúng số tiền
ex3 = look(name, amounts, "Ha", 10000)
print(ex3) #Kết quả ra False: có số tiền nhưng k có tên
ex4 = look(name, amounts, "Lap", 125000)
print(ex4) #Kết quả ra False: k có tên cũng như số tiền đó

#Case not use "in":
def look1(name, amounts, name1, money):
    result = False
    for i in range(len(name)):
        num1 = name[i]
        num2 = amounts[i]
        if num1 == name1 and num2 == money:
            return True
    return False
            
#Call function:
ex5 = look1(name, amounts, "Hoa", 15000)
print(ex5) #Kết quả ra False: có tên nhưng k đúng số tiền
ex6 = look1(name, amounts, "Binh", 10000)
print(ex6) #Kết quả ra False: có số tiền nhưng k có tên
ex7 = look1(name, amounts, "Nhi", 62000)
print(ex7) #Kết quả ra False: k có tên cũng như số tiền đó
ex8 = look1(name, amounts, "Dao", 1200000)
print(ex8) #Kết quả ra True
