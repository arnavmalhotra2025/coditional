#Activity 1
num = 3
if num > 0:
    print(num, "is a positive number")


num = -1
if num < 0:
    print(num, "is a negative number")
    
#Activity 2
actual_cost = float(input("Please enter the actual product price: "))
sale_amount = float(input("Please enter the sales Amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0}".format(amount))
    
else:
    print("no profit")
    
#Activity 3
i = int(input("enter a number:"))
if (i < 15 ):
    print("i is smaller than 15")
    print("i'm in if block")
    
else:
    print("i is greater than 15")
    print("i'm in else block")

print("i'm not in if Block not in else block")