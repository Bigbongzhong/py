import os

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)

    def __str__(self):
        low_stock_tag = " <LOW STOCK>" if self.quantity < 5 else ""
        return f"{self.product_id:<10} {self.name:<20} {self.quantity:<10} ${self.price:<10.2f}{low_stock_tag}"

    def to_csv(self):
        return f"{self.product_id},{self.name},{self.quantity},{self.price}\n"

    @staticmethod
    def from_csv(line):
        parts = line.strip().split(',')
        return Product(parts[0], parts[1], parts[2], parts[3])

class InventorySystem:
    def __init__(self, filename='inventory.csv'):
        self.filename = filename
        self.products = []
        self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip():  # ignore empty lines
                        self.products.append(Product.from_csv(line))

    def save_inventory(self):
        with open(self.filename, 'w') as file:
            for product in self.products:
                file.write(product.to_csv())

    def add_product(self, product):
        if any(p.product_id == product.product_id for p in self.products):
            print("Product ID already exists.")
            return
        self.products.append(product)
        self.save_inventory()
        print("Product added successfully.")

    def update_quantity(self, product_id, delta_qty):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity += delta_qty
                self.save_inventory()
                print(f"Quantity updated. New quantity: {product.quantity}")
                return
        print("Product ID not found.")

    def delete_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                confirm = input(f"Are you sure you want to delete '{product.name}'? (y/n): ").lower()
                if confirm == 'y':
                    del self.products[i]
                    self.save_inventory()
                    print("Product deleted.")
                else:
                    print("Deletion cancelled.")
                return
        print("Product ID not found.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
            return

        print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price':<10}")
        print("-" * 60)
        for product in self.products:
            print(product)

        print("\nLow Stock Items (quantity < 5):")
        found = False
        for product in self.products:
            if product.quantity < 5:
                print(f" - {product.name} (Qty: {product.quantity})")
                found = True
        if not found:
            print("All items sufficiently stocked.")

def display_menu():
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Delete Product")
    print("4. View Inventory")
    print("5. Exit")

def main():
    system = InventorySystem()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                qty = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))
                system.add_product(Product(pid, name, qty, price))
            except ValueError:
                print("Invalid input for quantity or price.")

        elif choice == '2':
            pid = input("Enter Product ID: ").strip()
            try:
                delta = int(input("Enter quantity to add/remove (e.g., 5 or -3): "))
                system.update_quantity(pid, delta)
            except ValueError:
                print("Invalid quantity.")

        elif choice == '3':
            pid = input("Enter Product ID to delete: ").strip()
            system.delete_product(pid)

        elif choice == '4':
            system.display_inventory()

        elif choice == '5':
            print("Exiting Inventory System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
