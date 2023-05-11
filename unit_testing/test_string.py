import unittest


# class name and inheritence 
class TestStringMethods(unittest.TestCase):

    # all methods must have self (this) as first parameter
    def test_upper(self):
        test_data = "foo"
        test_result = test_data.upper()
        self.assertEqual(test_result, "FOO")

    def test_is_upper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse(("foo".isupper()))

    def test_split(self):
        s = "Hello World"
        self.assertEqual(s.split(), ["Hello", "World"])

        # can test for exceptions thrown by code
        # execute code-block and make sure it raises the specified exception
        with self.assertRaises(TypeError):
            s.split(2)

# main program
if __name__ == "__main__":
    # python sets this variable to main if we are run from the shell
    unittest.main()