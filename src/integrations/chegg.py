import aiohttp
from requests_html import HTMLSession

class Chegg:
    def __init__(self, key):
        self.key = key

    async def search(self, isbn):
        # use self.key for your API auth
        # use with aiohttp to do the requests
        
        session = HTMLSession()
        r = session.get(f"https://www.ecampus.com/book/bk/{isbn}.html")
        
        price = r.html.find('.rental-price', first=True).text
        title = r.html.find('.title', first=True).text
        
        authors = r.html.find('.author a')
        author_list = []
        
        for author in authors:
            author_list.append(author.text)
        
        return {
            "price": price,
            "name": title,
            "authors": author_list
        }
