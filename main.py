from restaurant import Restaurant
from customer import Customer
from admin import Admin

def admin_menu(admin):
    while True:
        print("\n---admin menu---")
        print("1. Create customer account")
        print("2. Remove customer account")
        print("3. View all customers")
        print("4. Manage restaurant menu")
        print("5. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            admin.create_customer(name, email, address)
        elif choice == '2':
            email = input("Enter customer email to remove: ")
            admin.remove_customer(email)
        elif choice == '3':
            admin.view_customer()
        elif choice == '4':
            manage_menu(admin)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def manage_menu(admin):
    while True:
        print("\n---manage menu---")
        print("1. Add menu item")
        print("2. Remove menu item")
        print("3. Update menu item price")
        print("4. View menu")
        print("5. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            admin.add_menu_item(name, price)
        elif choice == '2':
            name = input("Enter item name to remove: ")
            admin.remove_menu_item(name)
        elif choice == '3':
            name = input("Enter item name to update: ")
            new_price = float(input("Enter new price: "))
            admin.update_menu_item(name, new_price)
        elif choice == '4':
            print("\n---restaurant menu---")
            for item, price in admin.menu.items():
                print(f"{item}: ${price}")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def customer_menu(customer, restaurant):
    while True:
        print(f"\n--- {customer.name}'s menu ----")
        print("1. View restaurant menu")
        print("2. View balance")
        print("3. Add balance")
        print("4. Place order")
        print("5. View past orders")
        print("6. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            print("\n---restaurant menu---")
            for item, price in restaurant.menu.items():
                print(f"{item}: ${price}")
        elif choice == '2':
            customer.check_balance()
        elif choice == '3':
            amount = float(input("Enter amount to add: "))
            customer.balance += amount
            print(f"${amount} added to your balance.")
        elif choice == '4':
            item_name = input("Enter item name to order: ")
            if item_name in restaurant.menu:
                price = restaurant.menu[item_name]
                if customer.balance >= price:
                    customer.balance -= price
                    customer.order_history.append(item_name)
                    print(f"Ordered {item_name} for ${price}")
                else:
                    print("Insufficient funds")
            else:
                print(f"{item_name} is not on the menu")
        elif choice == '5':
            customer.view_order_history()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def main():
    restaurant = Restaurant()
    admin = Admin(restaurant)
    
    while True:
        print("\n---restaurant Management System---")
        print("1. Admin login")
        print("2. Customer login")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            admin_name = input("Enter admin name: ")
            print(f"\nWelcome admin {admin_name}")
            admin_menu(admin)
        elif choice == '2':
            customer_name = input("Enter customer username: ")
            if customer_name in restaurant.customers:
                customer = restaurant.customers[customer_name]
                customer_menu(customer, restaurant)
            else:
                print("Customer not found.")
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")


main()