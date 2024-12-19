class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = {}
    
    def add_menu_item(self,item_name,price):
        self.menu[item_name] = price
        price(f"Added {item_name} to the menu for {price}")
    
    def remove_menu_item(self,item_name):
        if item_name in self.menu:
            del self.menu[item_name]
            print(f"Removed {item_name} from the menu")
        else:
            print(f"{item_name} is not in the menu")
    def show_menu(self):
        print("Menu: ")
        for item,price in self.menu.items():
            print(f"{item}: ${price}")
        return self.menu
    
    def add_customer(self,customer):
        if customer.email not in self.customers:
            self.customers[customer.email] = customer
            print(f"Added {customer.name} to the customer list")
        else:
            print(f"{customer.email} is already a customer")
    
    def customer_details(self,email):
        if email in self.customers:
            customer = self.customers[email]
            print(f"Customer: {customer.name}")
            print(f"Email: {customer.email}")
            print(f"Phone: {customer.phone}")
        else:
            print(f"{email} is not a customer")