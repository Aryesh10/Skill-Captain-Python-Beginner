class Product:
    def __init__(self, productName, productPrice, productQuantity):
        self.productName = productName
        self.productPrice = float(productPrice)
        self.productQuantity = int(productQuantity)

    def displayInfo(self):
        print(f"Product Name: {self.productName}")
        print(f"Product Price: ${self.productPrice:.2f}")
        print(f"Product Quantity: {self.productQuantity}")

class ProductRegistration:
    def __init__(self):
        self.product_database = []

    def register_product(self):
        print("\n=== Register a New Product ===")
        try:
            name = input("Enter product name: ").strip()

            while True:
                try:
                    price = float(input("Enter product price: ").strip())
                    if price <= 0:
                        raise ValueError("Price must be greater than zero.")
                    break
                except ValueError as e:
                    print(f"Invalid input for price. {e}")

            while True:
                try:
                    quantity = int(input("Enter product quantity: ").strip())
                    if quantity < 0:
                        raise ValueError("Quantity cannot be negative.")
                    break
                except ValueError as e:
                    print(f"Invalid input for quantity. {e}")

            new_product = Product(name, price, quantity)
            self.product_database.append(new_product)
            print("Product registered successfully!")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def display_products(self):
        print("\n=== Registered Products ===")
        if not self.product_database:
            print("No products registered.")
        else:
            for product in self.product_database:
                product.displayInfo()
                print("------------------")

if __name__ == "__main__":
    system = ProductRegistration()

    while True:
        print("\n1. Register a New Product")
        print("2. Display Registered Products")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: ").strip())
            match choice:
                case 1:
                    system.register_product()
                case 2:
                    system.display_products()
                case 3:
                    print("Exiting the system. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
