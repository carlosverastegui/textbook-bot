import aiohttp
from requests_html import HTMLSession

class Chegg:
    def __init__(self):
        pass

    async def search(self, isbn):
        session = HTMLSession()
        r = session.get(f"https://www.campusbooks.com/search/{isbn}?buysellrent=buy.html")

        title = r.html.find('h1 .page-header', first=True)
        vendors = r.html.find('tr')
        authors = r.html.find('dt')

        writer = ""
        price = ""

        for author in authors:
            auth = author.find('strong', first=True)

            if auth and auth.text == "Authors":
                writer = author.text
                break

        for vendor in vendors:
            tag = vendor.find('[title~=Chegg]', first=True)
   
            if tag:
                price = vendor.find('td .price', first=True).text
                break

        return {
            "price": price.replace('$', ''),
            "name": title,
            "authors": writer
        }
