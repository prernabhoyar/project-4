menu={'Pizza':120,'Pasta':70,'Cold drinks':40,'Burger':60,'French Fries':80,'Cholcolate Shake':100}
print("Welcome to Dior Cafe")
print("What do you want to order\nPizza:120\nPasta:70\nCold drinks:40\nBurger:60\nFrench Fries:80\nCholcolate Shake:100")
order_total=0
item1=input("Enter the item you want to order:")
if item1 in menu:
    order_total+=menu[item1]
    print(f"Order for {item1} successfully added.")
else:
    print(f"{item1} is not available")
another_order=input("Do you want to order more?(yes/no)")
if another_order=="yes":
    item_2=input("Enter the second item")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"{item_2} added successfully to the order")
    else:
        print(f"{item_2} is not available")
else:
    print(f"The total price of the order is: {order_total}")
    
