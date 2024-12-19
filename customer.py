class Customer:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.balance = 0
        self.order_history = []
    
    def add_funds(self,amount):
        self.balance += amount
        print(f"Added ${amount} to your balance")
    
    def view_menu(self,restaurant):
        return restaurant.show_menu()
    
    def place_order(self,restaurant,item_name):
        if item_name in restaurant.menu:
            price = restaurant.menu[item_name]
            if self.balance  >= price:
                self.balance -= price
                self.order_history.append(item_name)
                print(f"Ordered {item_name} for ${price}")
            else:
                print("Insufficient funds")
        else:
            print(f"{item_name} is not on the menu")

    def check_balance(self):
        print(f"Your balance is ${self.balance}")
    
    def view_order_history(self):
        print("order history: ")
        for item in self.order_history:
            print(item)