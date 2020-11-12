import aiohttp
import re
import urllib.parse

from aiohttp.client_exceptions import ContentTypeError
from utils import request



class Amazon:
    def __init__(self, key):
        self.key = key
        self.textsurf_regex = re.compile("url=(.*amazon).*Buy Used \$(.+)</a>")
        self.textsurf_title_regex = re.compile('<h1 class="h1">(.*)')
        self.textsurf_author_regex = re.compile("Author: (.+)")

    async def search(self, isbn):
        try:
            textsurf_page = await request(f"https://www.textsurf.com/details/{isbn}/-", json=False)

            textsurf_data = self.textsurf_regex.search(textsurf_page)
            textsurf_title_data = self.textsurf_title_regex.search(textsurf_page)
            textsurf_author_data = self.textsurf_author_regex.search(textsurf_page)

            if textsurf_data and textsurf_title_data:
                amazon_url = urllib.parse.unquote(textsurf_data.group(1))
                price = float(textsurf_data.group(2))
                title = textsurf_title_data.group(1)
                authors = textsurf_author_data.group(1) if textsurf_author_data else ""

                return {
                    "url": amazon_url,
                    "price": price,
                    "name": title,
                    "authors": authors,
                    "integration": "amazon"
                }


        except ContentTypeError:
            return None
