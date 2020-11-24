from aiounittest import async_test
import sys
import unittest

sys.path.append(".")

from src.integrations import Chegg

class TestCheggIntegration(unittest.TestCase):

    def setUp(self):
        self.chegg = Chegg()

    @async_test
    async def test_isbn_data_1(self):
        data = await self.chegg.search(9780471368793)

        # Make sure data was fetched
        self.assertIsNotNone(data)

        # Check the dictionary
        self.assertDictEqual(data, {"price": 42.99,
                                    "url": "https://www.campusbooks.com/search/9780471368793?buysellrent=buy.html",
                                    "name": "Abstract Algebra",
                                    "authors": "Herstein, I. N.",
                                    "integration": "chegg"})

    @async_test
    async def test_isbn_data_2(self):
        data = await self.chegg.search(9780134685991)

        # Make sure data was fetched
        self.assertIsNotNone(data)

        # Check the dictionary
        self.assertDictEqual(data, {"price": 34.99,
                                    "url": "https://www.campusbooks.com/search/9780134685991?buysellrent=buy.html",
                                    "name": "Effective Java",
                                    "authors": "Bloch, Joshua",
                                    "integration": "chegg"})

    @async_test
    async def test_invalid_isbn_1(self):
        data = await self.chegg.search(500)

        # Invalid ISBN
        self.assertIsNone(data)

    @async_test
    async def test_invalid_isbn_2(self):
        data = await self.chegg.search(9780321486813)

        # Book is not found on Chegg
        self.assertIsNone(data)

    @async_test
    async def test_invalid_isbn_3(self):
        data = await self.chegg.search(-10)

        # Invalid ISBN
        self.assertIsNone(data)


if __name__ == "__main__":
    unittest.main()
