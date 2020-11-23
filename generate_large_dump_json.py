from random import randint
import json


def create_item():
    item_id = randint(1, 100)
    items_amount = randint(1, 10)
    item_price = item_id * 727
    return {
        'item_id': item_id,
        'items_amount': items_amount,
        'item_price': item_price
    }


def create_customer():
    user_id = randint(1, 100)
    order_id = randint(1, 10000000000)
    items_no = randint(1, 20)
    items = [create_item() for item in range(items_no)]
    return {
        "user_id": user_id,
        "order_id": order_id,
        "items": items,
    }


mock = [create_customer() for x in range(10_000)]
with open('gen_data.json', 'w') as out:
    json.dump(mock, out)
