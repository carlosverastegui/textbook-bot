import aiohttp


class Pearson:
    def __init__(self, key):
        self.key = key

    async def search(self, isbn):
        # use self.key for your API auth
        # use with aiohttp to do the requests
        try: 
            session = HTMLSession()
            r = session.get(f"https://www.pearson.com/store/en-us/search.html?_charset_=UTF-8&q={isbn}")
            price = r.html.find('.selected-product__price', first=True).text


            title = r.html.find('.product-summary__heading', first=True).text
            author = r.html.find('.product-authors', first=True).text

            return {
                "price": price,
                "name": title,
                "authors": author
            }
        
        except:
            return None 

