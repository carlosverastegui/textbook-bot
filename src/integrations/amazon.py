import aiohttp
import re

from aiohttp.client_exceptions import ContentTypeError
from utils import request



class Amazon:
    def __init__(self, key):
        self.key = key
        self.amazon_regex = re.compile('href="(.+)" rel="nofollow" target="_blank">Amazon</a></td><td><b><span id="p_amazon">\$(.+)</span>')

    async def search(self, isbn):
        try:
            book_data = await request(f"https://api.itbook.store/1.0/books/{isbn}")

            title = book_data.get("title")
            authors = book_data.get("authors")
            url = book_data.get("url")
            isbn10 = book_data.get("isbn10")

            if url:
                book_page = await request(url, json=False)
                amazon_search = self.amazon_regex.search(book_page)

                if amazon_search:
                    #amazon_url = f"https://itbook.store/{amazon_search.group(1)}
                    amazon_url = f"https://www.amazon.com/gp/product/{isbn10}"
                    price = amazon_search.group(2)

                    return {
                        "price": float(price),
                        "name": title,
                        "authors": authors,
                        "url": amazon_url
                    }

        except ContentTypeError:
            return None
