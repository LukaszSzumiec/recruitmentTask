from unittest import TestCase
from main_recruitment_task import AdvancedCalculationClass
import pathlib


class TestAdvancedCalculationClass(TestCase):

    def setUp(self) -> None:    
        path = pathlib.Path('data.json')
        calculation_class = AdvancedCalculationClass()
        calculation_class.load(path)
        self.obj = calculation_class

    def test_calculate_amount_of_one_order(self):
        mocked_data = [

            {
                "item_id": 18,
                "items_amount": 1,
                "item_price": 10
            },
            {
                "item_id": 12,
                "items_amount": 2,
                "item_price": 10
            }

        ]
        amount = self.obj.calculate_amount_of_one_order(mocked_data)
        self.assertEqual(amount, 30)

    def test_calculate_total_amount_of_money_spend_by_all_customers(self):
        amount = self.obj.calculate_total_amount_of_money_spend_by_all_customers()
        self.assertEqual(amount, 100)

    def test_calculate_total_amount_of_money_spent_by_a_customer(self):
        amount = self.obj.calculate_total_amount_of_money_spent_by_a_customer(25)
        self.assertEqual(amount, 100)

    def test_calculate_count_of_distinct_customers_by_item(self):
        count = self.obj.calculate_count_of_distinct_customers_by_item()
        self.assertDictEqual(count, {18: [25, 25], 12: [25, 25]})

    def test_get_items_amount_in_order(self):
        mocked_data = {
            'order_id': 1,
            'items': [
                {},
                {}
            ]
        }
        items_amount_in_order = self.obj.get_items_amount_in_order({}, mocked_data)
        self.assertDictEqual(items_amount_in_order, {1: 2})

    def test_calculate_items_amount_per_order(self):
        items_amount_per_order = self.obj.calculate_items_amount_per_order()
        self.assertDictEqual(items_amount_per_order, {6400342072: 2, 124134: 2})
