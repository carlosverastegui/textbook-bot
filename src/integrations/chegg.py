import aiohttp


class Chegg:
    def __init__(self, key):
        self.key = key

    async def search(self, isbn):
        # use self.key for your API auth
        # use with aiohttp to do the requests

        return {
            "price": 500,
            "name": "test item"
        }
