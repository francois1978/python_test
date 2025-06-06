from test1.product_item import ProductItem


class ProductItemGeneratorForTest:

    @staticmethod
    def generate_items() -> list[ProductItem]:
        return [
            #Customer 1
            ProductItem(order_id=1, customer_id="C01", order_date="2025-06-01", product_id="P01", category="Book",
                        price=10.0, quantity=1),
            ProductItem(order_id=2, customer_id="C01", order_date="2025-07-01", product_id="P02", category="Book",
                        price=10.0, quantity=1),
            ProductItem(order_id=2, customer_id="C01", order_date="2025-07-01", product_id="P056", category="Book",
                        price=10.0, quantity=1),
            ProductItem(order_id=2, customer_id="C01", order_date="2025-07-01", product_id="P089", category="Book",
                        price=10.0, quantity=1),
            ProductItem(order_id=3, customer_id="C01", order_date="2025-06-01", product_id="P03", category="PS5",
                        price=10.0, quantity=2),
            # Customer 2
            ProductItem(order_id=4, customer_id="C02", order_date="2025-08-01", product_id="P04", category="XBOX",
                        price=10.0, quantity=1),
            ProductItem(order_id=5, customer_id="C02", order_date="2025-07-01", product_id="P05", category="TV",
                        price=10.0,
                        quantity=1),
            ProductItem(order_id=6, customer_id="C02", order_date="2025-10-01", product_id="P06", category="Book",
                        price=10.0, quantity=1),
            # Customer 3
            ProductItem(order_id=6, customer_id="C03", order_date="2025-06-01", product_id="P07", category="Book",
                        price=10.0, quantity=1),
            ProductItem(order_id=6, customer_id="C03", order_date="2025-11-01", product_id="P08", category="Book",
                        price=10.0, quantity=2),
            ProductItem(order_id=6, customer_id="C03", order_date="2025-06-01", product_id="P03", category="PS5",
                        price=10.0, quantity=1),
            # Customer 4
            ProductItem(order_id=6, customer_id="C04", order_date="2025-01-01", product_id="P09", category="Book",
                        price=10.0, quantity=2),
            ProductItem(order_id=6, customer_id="C05", order_date="2025-03-01", product_id="P10", category="Pet",
                        price=10.0, quantity=1)]
