from customer import Customer
class Admin:
    def __init__(self,restaurant):
        self.menu = restaurant.menu
        self.customers = restaurant.customers
    
    def create_customer(self,name,email,phone):
        if email not in self.customers:
            customer = Customer(name,email,phone)
            self.customers[email] = customer
            print(f"Created customer {name}")
        else:
            print(f"{email} is already a customer")
    
    def view_customer(self):
        if not self.customers:
            print("No Customers")
        else:
            for email,customer in self.customers.items():
                print(f"Name: {customer.name}, Email: {email}, Phone: {customer.phone}")
    
    def remove_customer(self,email):
        if email in self.customers:
            del self.customers[email]
            print(f"Removed customer {email}")
        else:
            print(f"{email} is not a customer")
    
    def add_menu_item(self,name,price):
        if name in self.menu:
            print(f"{name} is already in the menu")
        else:
            self.menu[name] = price
            print(f"Added {name} to the menu")
    
    def remove_menu_item(self,name):
        if name in self.menu:
            del self.menu[name]
            print(f"Removed {name} from the menu")
        else:
            print(f"{name} is not in the menu")
    
    def update_menu_item(self,name,new_price):
        if name in self.menu:
            self.menu[name] = new_price
            print(f"Updated {name} price to {new_price}")
        else:
            print(f"{name} is not in the menu")
        

    
    

