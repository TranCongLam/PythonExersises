#Exercise 1:
#Case 1:
def remove_even(num_list):
    if len(num_list) == 0:
        return 0
    for i in range(len(num_list) - 1, -1, -1):
        num = num_list[i]
        if num % 2 == 0:
            num_list.remove(num)
    print("List of odd number", num_list)
        
#Example 1:
num_list1 = [1, 2, 4, 6, 7, 9]
remove_even(num_list1)
#Example 2:
num_list2 = []
remove_even(num_list2)

#Case 2:
def remove_even1(num_list):
    new_list = []
    if len(num_list) == 0:
        return 0
    for i in range(len(num_list)):
        num = num_list[i]
        if num % 2 != 0:
            new_list.append(num)
    print("List of odd number", new_list)       
        

#Example 1:
num_list3 = [12, 14, 13, 35, 38, 40]
remove_even1(num_list3)
#Example 2:
num_list4 = []
remove_even1(num_list4)

#Exercise 2:
def donate(donate_list, name):
    totalMoney = 0
    if len(donate_list) == 0:
        return None
    for i in range(len(donate_list)):
        name1 = donate_list[i][0]
        if name1 == name:
            totalMoney += donate_list[i][1]
    return totalMoney

donate_list = [("Duong", 109090), ("Huy", 1097), ("Vu", 98000), ("Duong", 80090), ("Vu", 698000)]
#Example 1:
totalAmount = donate(donate_list, "Vu")
print(totalAmount)
#Example 2:
totalAmount1 = donate(donate_list, "Huy")
print(totalAmount1)
#Example 3:
donate_list1 = []
totalAmount2 = donate(donate_list1, "Huy")
print(totalAmount2)



#Exercise 3: Thanh toan sinh hoat phi
def totalBill(totalAmounts, bills):
    if len(bills) == 0 and totalAmounts == 0 :
        print("This month you stay at home and your parents pay bills")
    elif len(bills) > 0 and totalAmounts == 0:
        print("You have to work part-time to get money")
    elif len(bills) == 0 and totalAmounts > 0 :
        print("This month you stay at home and your parents give you money")
    else: 
        totalMoney = 0
        for i in range(len(bills)):
            money = bills[i][1]
            totalMoney += money
        print("The amount you used is:", totalMoney)
        remainDebt = totalMoney - totalAmounts 
        if totalAmounts >= totalMoney:
            remainDebt = 0
            print("You used your money very reasonable this month and Money remain debt is:", remainDebt)
            return True
        else:
            print("You dont't used your money very reasonable this month and Money remain debt is:", remainDebt)
            return False
    
#Example 1:
totalAmount1 = 1500000
bills1 = [("Electric", 200000), ("Water", 60000), ("Food", 1200000), ("Entertainment", 300000)]
notice = totalBill(totalAmount1, bills1)
print(notice)

#Example 2:
totalAmount2 = 1500000
bills2 = [("Electric", 150000), ("Water", 50000), ("Food", 1050000), ("Entertainment", 120000)]
notice1 = totalBill(totalAmount2, bills2)
print(notice1)

#Example 3:
totalAmount3 = 1500000
bills3 = []
totalBill(totalAmount3, bills3)

#Example 4:
totalAmount4 = 0
bills4 = []
totalBill(totalAmount4, bills4)
