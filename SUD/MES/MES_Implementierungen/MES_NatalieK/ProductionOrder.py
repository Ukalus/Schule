class ProductionOrder:
    def __init__(self, order_number: int, product_name: str, quantity: int):
        self.__order_number: int = order_number
        self.__product_name: str = product_name
        self.__quantity: int = quantity
        self.__status: str = "created"
        self.__produced_units: int = 0
        print("Order created.")
        self.print_status()

    def get_order_number(self):
        return self.__order_number

    def start(self):
        if not self.__status == "created":
            raise ValueError(f"Cannot start order. Current status: '{self.__status}'")
        self.__status = "started"
        self.print_status()
        

    def finish(self):
        if not self.__produced_units >= self.__quantity:
            raise ValueError(f"Cannot finish order. Required amount: '{self.__quantity}' Amount produced: '{self.__produced_units}'")
        #interessant wäre zu viel produzierte Produkte in ein Lager zu legen und dann ebenfalls wieder zu verwerten
        self.__status = "finished"
        self.print_status()

    def produce(self, units: int):
        if not self.__status == "started":
            raise ValueError(f"Cannot produce '{self.__product_name}'. Current order status: '{self.__status}'")
        self.__produced_units += units
        
    def get_production_efficiency(self):
        if self.__produced_units == 0:
            return 0
        return round((self.__produced_units / self.__quantity) * 100, 2)
    
    def print_status(self):
        print("Current order status: " + self.__status)
