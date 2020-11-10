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
        authors = r.html.find('.author a', first=True).text
        #password = 1
        #book_data = await request(f"http://api.chegg.com/rent.svc?KEY={self.key}&PW={password}&isbn={isbn}&R=JSON&with_pids=1&page=1&results_per_page=10&V=4.0")
        
        #book_info = book_data.get('Items')[0]
        #title = temp.get('BookInfo', {}).get('Title') 
        #price = temp.get('BookInfo', {}).get('ListPrice') 
        #authors = temp.get('BookInfo', {}).get('Authors') 
        
        return {
            "price": price,
            "name": title,
            "authors": authors
        }