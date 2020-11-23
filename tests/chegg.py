import unittest
import sys
from aiounittest import async_test

sys.path.append(".") # so we can load the integrations

from src.integrations import Chegg

class TestCheggIntegration(unittest.TestCase):

    def setUp(self):
        self.chegg = Chegg()

    @async_test
    async def test_valid_isbn_1(self):
        data = await self.chegg.search(9780134609935)

        self.assertIsNotNone(data)

        self.assertEqual(data["name"], "Earth Science")

        self.assertTrue("chegg" in data["url"])

    @async_test
    async def test_valid_isbn_2(self):
        data = await self.chegg.search(9781617294136)

        self.assertIsNotNone(data)

        self.assertEqual(data["name"], "Securing DevOps: Security in the Cloud")

        self.assertTrue("chegg" in data["url"])

    @async_test
    async def test_valid_isbn_3(self):
        data = await self.chegg.search(9780201000238)

        self.assertIsNotNone(data)

        self.assertEqual(data["name"], "Data Structures and Algorithms")

        self.assertTrue("chegg" in data["url"])

    @async_test
    async def test_invalid_isbn_1(self):
        data = await self.chegg.search(500)

        self.assertIsNone(data)

    @async_test
    async def test_invalid_isbn_2(self):
        data = await self.chegg.search(-1)

        self.assertIsNone(data)



if __name__ == "__main__":
    unittest.main()
