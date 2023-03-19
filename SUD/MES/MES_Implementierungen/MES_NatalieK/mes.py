import ProductionOrder
import mes_utils
import ProductionLine

class MES:
    def __init__(self):
        self.__productionLine_List: list = []

    def add_production_line(self, name:str):
        self.__productionLine_List.append(ProductionLine.ProductionLine(name))

    def create_production_order(self, production_line_name: str, order_number:int, product_name: str, quantity: int):
        production_line: ProductionLine = self.get_production_line(production_line_name)

        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order: ProductionOrder = ProductionOrder.ProductionOrder(order_number, product_name, quantity)
        production_line.add_order(order)

    def start_production_order(self, production_line_name: str, order_number: int):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order: ProductionOrder = mes_utils.mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.start()
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    def finish_production_order(self, production_line_name: str, order_number: int):
        production_line: ProductionLine = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order: ProductionOrder = mes_utils.mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.finish()
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    def produce_units(self, production_line_name: str, order_number: int, units: int):
        production_line: ProductionLine = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order: ProductionOrder = mes_utils.mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.produce(units)
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    def get_production_lines(self):
        return self.__productionLine_List

    def get_production_line(self, name: str):
        for line in self.__productionLine_List:
            if line.get_production_line_name() == name:
                return line
