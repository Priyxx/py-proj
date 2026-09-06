 #define the menu of hotel - Priyanshu Purohit 
menu = {
    'pizza': 40,
    'pasta': 66,
    'burger': 55,
    'drink':100,
    'momos': 60,

}

print("padharo sahhhh!!!")
print("Pizza : Rs 40\nPasta : Rs 66\nBurger: Rs 55\nDrink : Rs 100\nMomos : Rs 60\n")

order_total = 0
#66+50
item_1 = input("enter item name = ")
if item_1 in menu:
    order_total += menu[item_1] # 0+ pizza 40
    print(f"your item {item_1} has been added to cart ")
else:
    print(f"ordered item {item_1} not available ")

another_order = input("do u want to add another item ? (yes/no) ")
if another_order =="yes":
        item_2 = input("enter item 2 name = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"item {item_2} added in cart")
        else:
            print(f"ordered item {item_2} is not in menu")

print(f"total amount = {order_total}")
