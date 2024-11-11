import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(11), 50)
       
    # Add your additional test cases here.

    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(56), 150)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_invalid_negative_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid age")
    
    def test_invalid_age_zero(self):
        self.assertEqual(self.zoo.get_ticket_price(0), "Invalid age")

    def test_teenager_on_boundary(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    
    def test_adult_on_boundary(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_senior_on_boundary(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    

if __name__ == '__main__':
    unittest.main()
