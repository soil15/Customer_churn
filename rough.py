import pandas as pd
import numpy as np
from dataclasses import dataclass


@dataclass
class TestDataClass:

    var_one = 1
    var_two = 2


class TestClass:

    def __init__(self):

        self.data_class_obj = TestDataClass()

    def test_method_two(self, val):

        print(self.data_class_obj.var_two, val)

    def test_method_one(self):

        print(self.data_class_obj.var_one)
        self.test_method_two(4)



if __name__ == '__main__':

    test_class_obj = TestClass()
    test_class_obj.test_method_one()