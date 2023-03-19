class ProductionOrder:
    def __init__(self, order_number, product_name, quantity):
        self.__order_number = order_number
        self.__product_name = product_name
        self.__quantity = quantity
        self.__status = "created"
        self.__produced_units = 0

    def get_order_number(self):
        return self.__order_number
    def start(self):
        self.__status = "running"
    def finish(self):
        self.__produced_units = self.__quantity
        self.__status = "finished"

    def produce(self, units):
        self.__quantity = units
    def get_production_efficiency(self):

        return round((self.__produced_units / self.__quantity) * 100, 2)


class ProductionLine:
    def __init__(self, name):
        self.__production_line_name = name
        self.__orders = []

    def add_order(self, order):
        self.__orders.append(order)
    
    def get_production_line_name(self):
        return self.__production_line_name
    def get_orders(self):
        return self.__orders

class MES:
    __production_lines: list[ProductionLine]
    def __init__(self):
        self.__production_lines = []
    def add_production_line(self, name):
        self.__production_lines.append(ProductionLine(name))
    def create_production_order(self, production_line_name, order_number:int, product_name, quantity):

        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = ProductionOrder(order_number, product_name, quantity)
        production_line.add_order(order)

    def start_production_order(self, production_line_name, order_number):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.start()
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    def finish_production_order(self, production_line_name, order_number):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.finish()
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    def produce_units(self, production_line_name, order_number, units):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.produce(units)
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    
    def get_production_lines(self):
        return self.__production_lines

    def get_production_line(self, name):
        for i in range(0,self.__production_lines.count()):
            if self.__production_lines[i].get_production_line_name() == name
        return self.__production_lines[self.__production_lines]


class mes_utils:

    @staticmethod
    def get_order_by_number(production_line, order_number):
        order_list  = production_line.get_orders()
        for order in order_list:
            if order.get_order_number() == order_number:
                return order
        raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line.get_production_line_name()}'")

        

    @staticmethod
    def calculate_production_efficiency(order):
        return order

#from mes import MES, ProductionOrder, ProductionLine, mes_utils

# Erstelle eine MES-Instanz
mes = MES()

# Füge eine Produktionslinie hinzu
mes.add_production_line("Produktionslinie 1")

# Erstelle eine Bestellung
mes.create_production_order("Produktionslinie 1", 1001, "Produkt 1", 100)

# Starte den Produktionsauftrag
mes.start_production_order("Produktionslinie 1", 1001)

# Produziere Einheiten für einen Auftrag
mes.produce_units("Produktionslinie 1", 1001, 50)

# Beende den Produktionsauftrag
mes.finish_production_order("Produktionslinie 1", 1001)

# Berechne die Produktionseffizienz des Produktionsauftrags
#order = mes_utils.get_order_by_number(mes.production_lines["Produktionslinie 2"], 1001)
order = mes_utils.get_order_by_number(mes.get_production_line("Produktionslinie 1"), 1001)
efficiency = mes_utils.calculate_production_efficiency(order)

print(f"Die Produktionseffizienz des Auftrags ist {efficiency}%.")
