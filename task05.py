class Product:
    def __init__(self, name: str, price: float, category: str, in_stock: bool):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
        
        

product1 = Product("iPhone 15", 12999.99, "electronics", True)
product2 = Product("Nike Air Max", 899.50, "clothing", False)

print("Mahsulot:", product1.name, "| Narxi:", product1.price)
print("Mahsulot:", product2.name, "| Narxi:", product2.price)