class Vehicle:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")

class Truck(Vehicle):
    def __init__(self,brand, model, capacity):
        super().__init__(brand,model)
        self.load_capacity=capacity

    def display_info(self):
        print(f"Load Capacity : {self.load_capacity} tons")
        return super().display_info()
    
    
        
obj1=Truck("Tata", "Bull", 100)
obj2=Truck("Ashok Leyland", "Huge", 150)

obj1.display_info()
obj2.display_info()