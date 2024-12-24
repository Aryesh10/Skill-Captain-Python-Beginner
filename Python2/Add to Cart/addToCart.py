class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"


class Cart:
    def __init__(self, username):
        self.username = username
        self.products = []

    def add_to_cart(self, product, quantity):
        if quantity > 0 and quantity <= product.quantity:
            self.products.append(Product(product.name, product.price, quantity))
            product.quantity -= quantity
            return True
        return False

    def remove_from_cart(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False

    def display_cart(self):
        if not self.products:
            return f"{self.username}'s cart is empty."
        return "\n".join(str(product) for product in self.products)


def main():
    available_products = [
        Product("Laptop", 999.99, 10),
        Product("Mouse", 19.99, 50),
        Product("Keyboard", 49.99, 30),
        Product("Headphones", 79.99, 20),
        Product("Monitor", 199.99, 15)
    ]
    
    cart = Cart(input("Enter your name: "))
    while True:
        print("\nMenu:")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. Display Cart")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\nAvailable Products:")
                for idx, product in enumerate(available_products, start=1):
                    print(f"{idx}. {product}")
            case "2":
                print("\nEnter the number of the product you want to add:")
                for idx, product in enumerate(available_products, start=1):
                    print(f"{idx}. {product}")
                product_choice = int(input("Your choice: ")) - 1
                if 0 <= product_choice < len(available_products):
                    selected_product = available_products[product_choice]
                    quantity = int(input(f"Enter quantity for {selected_product.name} (Available: {selected_product.quantity}): "))
                    if cart.add_to_cart(selected_product, quantity):
                        print(f"{quantity} {selected_product.name}(s) added to cart.")
                    else:
                        print(f"Invalid quantity. Please enter a value between 1 and {selected_product.quantity}.")
                else:
                    print("Invalid choice. Please try again.")
            case "3":
                product_name = input("Enter product name to remove: ")
                if cart.remove_from_cart(product_name):
                    print(f"{product_name} removed from cart.")
                else:
                    print(f"{product_name} not found in cart.")
            case "4":
                print(cart.display_cart())
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
