"""
Test for source.source2
"""
from source.source2 import get_quadrilateral_type
from unittest import TestCase

class TestGetQuadrilateralType(TestCase):

    def test_get_quadrilateral_square_list(self):
        a = [2, 2, 2, 2]
        result = get_quadrilateral_type(a)
        self.assertEqual(result, 'square') 

    def test_get_quadrilateral_square_all_int(self):
        result = get_quadrilateral_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_rectangle_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_invalid_all_negative_int(self):
        result = get_quadrilateral_type(-1, -1, -1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_invalid_unequal_sides(self):
        result = get_quadrilateral_type(1, 1, 2, 1)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_invalid_combo_int_string(self):
        result = get_quadrilateral_type('a', 0, -1, -0)
        self.assertEqual(result, 'invalid')
    
    def test_get_quadrilateral_square_dict(self):
        result = get_quadrilateral_type({'a': 1, 'b': 1, 'c': 1, 'd': 1})
        self.assertEqual(result, 'square')

     


    

    

