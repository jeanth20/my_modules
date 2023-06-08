import uuid


class Product:

    CALORIES_TO_KJ = 4.184

    def __init__(self, name, calories, price_per_kg):
        self.name = name
        self.calories = calories
        self.price_per_kg = price_per_kg
        
    def do_something(self):
        print(self.name)
        pass
    
    def get_price(self, kg):
        return self.price_per_kg * kg
    
    def get_kilojoules(self):
        return self.calories * self.CALORIES_TO_KJ

    @staticmethod
    def generate_unique_id():
        return f"Product-{uuid.uuid4().hex}"

        
banana = Product("banana", calories=105, price_per_kg=1)
tomato = Product("tomato", calories=18, price_per_kg=2)
potato = Product("potato", calories=77, price_per_kg=1.5)
# print(banana.name, banana.calories)
# print(tomato.name, tomato.calories)
# banana.do_something()

# print(tomato.get_price(2))
# print(potato.get_price(1.5))

# print(f"kilojoule of {banana.name} is {banana.get_kilojoules()}")

print(Product.generate_unique_id())