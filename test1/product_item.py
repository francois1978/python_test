from dataclasses import dataclass
from datetime import date

@dataclass
class ProductItem:

    order_id: int
    customer_id: str
    order_date: str
    product_id: str
    category: str
    price: float
    quantity: int


