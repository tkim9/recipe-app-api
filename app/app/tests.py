# django frame work would looks for any file that starts with tests...
# as a unit test

from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):
    
    # test function should all begin with test_.. for django
    # if it has other name, django would not run this test
    def test_add_numbers(self):
        """Test that two numbers a added together"""
        self.assertEqual(add(3,8), 11)
        
    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5,11), 6)
        
    
        