# test the nice_thing module
import unittest
import nice_thing

class TestNiceThing1(unittest.TestCase):

    def setUp(self):
        # this runs before the tests in this test class
        self.nice_thing = nice_thing.NiceThing(1)

    def test_calories(self):
        self.assertEqual(756,self.nice_thing.calories())

class TestNiceThing10(unittest.TestCase):

    def setUp(self):
        # this runs before the tests in this test class
        self.nice_thing = nice_thing.NiceThing(10)

    def test_calories(self):
        self.assertEqual(7560,self.nice_thing.calories())

# MAIN PROGRAM
if __name__ == "__main__":
        unittest.main()