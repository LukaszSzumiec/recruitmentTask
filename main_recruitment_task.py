import json
from functools import reduce
from itertools import chain
import pathlib


class AdvancedCalculationClass:
    def __init__(self):
        self.data = None

    def load(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            self.data = json.loads(file.read())

    @classmethod
    def calculate_amount_of_one_order(cls, order: dict) -> dict:
        return reduce((lambda money_spent_sum, obj:
                       money_spent_sum + obj['items_amount'] * obj['item_price']), order, 0)

    def calculate_total_amount_of_money_spend_by_all_customers(self) -> dict:
        return reduce((lambda money_spent_sum, obj:
                       money_spent_sum + self.calculate_amount_of_one_order(obj.get('items'))), self.data, 0)

    def calculate_total_amount_of_money_spent_by_a_customer(self, customer_id: int) -> int:
        iterator = filter((lambda order: order if order.get('user_id') == customer_id else None), self.data)
        items = map(lambda item: item.get('items'), iterator)
        items = chain.from_iterable(items)
        return reduce((lambda sum_amount, item:
                       sum_amount + item.get('items_amount') * item.get('item_price')), items, 0)

    def calculate_count_of_distinct_customers_by_item(self) -> dict:
        items = dict()
        for order in self.data:
            for item in order.get('items'):
                if item['item_id'] in items:
                    items[item['item_id']].append(order.get('user_id'))
                else:
                    items[item['item_id']] = [order['user_id']]
        return items

    @classmethod
    def get_items_amount_in_order(cls, items_amount: dict, order: dict) -> dict:
        items_amount.update({order.get('order_id'): len(order.get('items'))})
        return items_amount

    def calculate_items_amount_per_order(self) -> dict:
        return reduce(self.get_items_amount_in_order, self.data, {})


if __name__ == '__main__':
    resource_file = pathlib.Path('data.json')
    # second_resource_file = pathlib.Path('gen_data.json')
    calculation_obj = AdvancedCalculationClass()
    calculation_obj.load(resource_file)
    # calculation_obj.load(second_resource_file)
    calculation_obj.calculate_total_amount_of_money_spend_by_all_customers()
    calculation_obj.calculate_total_amount_of_money_spent_by_a_customer(25)
    calculation_obj.calculate_count_of_distinct_customers_by_item()
    calculation_obj.calculate_items_amount_per_order()
