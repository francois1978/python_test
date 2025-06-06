import time

import pytest

from test1.processor import Processor
from typing import List

from test1.product_item import ProductItem
from test1.product_item_generator_for_test import ProductItemGeneratorForTest


class TestProcessor:


    def test_processor(self):
        start = time.time()

        #Write test code here
        processor = Processor()
        result = processor.compute_count_optimized(ProductItemGeneratorForTest.generate_items(), 1)

        # Calculate the end time and time taken
        end = time.time()
        length = end - start

        # Show the results : this can be altered however you like
        print("It took", length, "seconds")

        assert result == 2
