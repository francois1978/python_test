from itertools import groupby
from typing import List

from test1.product_item import ProductItem


class Processor():

    def compute_count_short_solution(self, product_items: List[ProductItem], count_per_customer: int) -> int:
        filtered_list = list(filter(lambda item: item.category == "Book", product_items))
        counter: int = 0
        for key, item_list in groupby(filtered_list, key=lambda item: item.customer_id):
            if len(list(item_list)) > count_per_customer:
                counter += 1
        return counter

    def compute_count_optimized(self, product_items: List[ProductItem], count_per_customer: int) -> int:
        # Code to complete

        customer_matching_condition = set()

        global_count: int = 0
        number_of_books_by_customer: dict[str, int] = {}

        for product_item in product_items:
            if product_item.category == "Book":
                number_of_books_by_customer.setdefault(product_item.customer_id, 0)
                count = number_of_books_by_customer.get(product_item.customer_id)
                count = count + 1
                number_of_books_by_customer[product_item.customer_id] = count
                if count > count_per_customer and (product_item.customer_id not in customer_matching_condition):
                    global_count = global_count + 1
                    customer_matching_condition.add(product_item.customer_id)

        return global_count
