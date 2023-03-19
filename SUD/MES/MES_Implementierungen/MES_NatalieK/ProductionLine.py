import ProductionOrder

class ProductionLine:
    def __init__(self, name: str):
        self.__production_line_name: str = name
        self.__orders: list = []
        print("Production line created.")

    def add_order(self, order: ProductionOrder):
        for o in self.__orders:
            if o.get_order_number() == order.get_order_number:
                raise ValueError(f"Order '{order.get_order_number()}' already exists.")
        self.__orders.append(order)
        print("Order added.")
    
    def get_production_line_name(self):
        return self.__production_line_name

    def get_orders(self):
        return self.__orders