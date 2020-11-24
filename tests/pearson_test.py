import unittest
import sys
from aiounittest import async_test

sys.path.append(".") # so we can load the integrations

from src.integrations import Pearson

class TestPearsonIntegration(unittest.TestCase):

    def setUp(self):
        self.pearson = Pearson()

    @async_test
    async def test_valid_isbn_1(self):
        data = await self.pearson.search(9780134439020)

        self.assertIsNotNone(data)

        self.assertEqual(data["name"], "Thomas' Calculus: Early Transcendentals, 14th edition")
        self.assertEqual(data["price"], "$223.99") 
        self.assertEqual(data["authors"], "Joel R. Hass\nChristopher Heil\nMaurice D. Weir") 

        self.assertTrue("pearson" in data["url"])

    @async_test
    async def test_valid_isbn_2(self):
        data = await self.pearson.search(9780133943030)

        self.assertIsNotNone(data)

        self.assertEqual(data["name"], "Software Engineering, 10th edition")
        self.assertEqual(data["authors"], "Ian Sommerville")
        self.assertEqual(data["price"], "$154.66") 

        self.assertTrue("pearson" in data["url"])

    @async_test
    async def test_valid_isbn_3(self):
        data = await self.pearson.search(9780134845623)

        self.assertIsNotNone(data)

        self.assertEqual(data["name"], "Machine Learning with Python for Everyone, 1st edition")
        self.assertEqual(data["price"], "$49.99")
        self.assertEqual(data["authors"], "Mark Fenner") 

        self.assertTrue("pearson" in data["url"])

    @async_test
    async def test_invalid_isbn_1(self):
        data = await self.pearson.search(123)

        self.assertIsNone(data)

    @async_test
    async def test_invalid_isbn_2(self):
        data = await self.pearson.search("abc")

        self.assertIsNone(data)



if __name__ == "__main__":
    unittest.main()
