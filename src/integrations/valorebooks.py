import aiohttp


class Pearson:
    def __init__(self, key):
        self.key = key

    async def search(self, isbn):
        # use self.key for your API auth
        # use with aiohttp to do the requests
        try:
            book_data = await request(f"https://api.valorebooks.com/sellback/pricing/best/{isbn}")

            return {
                "price": book_data.get("price")

             }
        except ContentTypeError:
            return None
