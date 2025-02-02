manu = {'pizza': 40,
        'pasta': 50,
        'salad': 60,
        'coffee': 70,
        'burger': 80, }

print("Welcome to python restaurant")
print(manu)
order_total = 0
item_1 = input("enter the name of item you want to order= ")

if item_1 in manu:
    order_total += manu[item_1]
    print(f"your item has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item?(yes/no)")
if another_order == 'yes':
    item_2 = input("Enter the name of second item= ")
    if item_2 in manu:


        print(f"item{item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")
print(f"the total amount of item to pay is {order_total}")
