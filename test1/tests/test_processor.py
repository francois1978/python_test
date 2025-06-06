import pytest

from test1.processor import Processor
from typing import List

from test1.product_item import ProductItem
from test1.product_item_generator_for_test import ProductItemGeneratorForTest


class TestProcessor:


    def test_processor(self):

        #Write test code here
        processor = Processor()
        result = processor.compute_count_short_solution(ProductItemGeneratorForTest.generate_items(), 1)
        assert result == 2
