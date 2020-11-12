import aiohttp
from requests_html import HTMLSession

class Chegg:
    def __init__(self, key):
        self.key = key

    async def search(self, isbn):
        # use self.key for your API auth
        # use with aiohttp to do the requests
        '''
        session = HTMLSession()
        r = session.get(f"https://www.ecampus.com/book/bk/{isbn}.html")
        
        price = r.html.find('.rental-price', first=True).text
        title = r.html.find('.title', first=True).text
        
        authors = r.html.find('.author a')
        author_list = []
        
        for author in authors:
            author_list.append(author.text)
        '''
        session = HTMLSession()
        r = session.get('https://www.chegg.com/textbooks/book-9781305657960-1305657969.html')

        price_pane = r.html.find('.purchase-option-content C-pdpv2-purchaseOption-buy', first=True)
        price = price_pane.find('.total-price', first=True)

        name = r.html.find('.name', first=True)
        authors = r.html.find('.txt-2 pdp-details-value span')
        author_list = []

        for author in authors:
           author_list.append(author.find(a, first=True).text)
        
        return {
            "price": price,
            "name": title,
            "authors": author_list
        }
