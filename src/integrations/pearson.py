from requests_html import HTMLSession


class Pearson:
    def __init__(self):
        pass

    async def search(self, isbn):
        try:
            session = HTMLSession()
            url = f"https://www.pearson.com/store/en-us/search.html?_charset_=UTF-8&q={isbn}"
            r = session.get(url)
            price = float((r.html.find('.selected-product__price', first=True).text).replace("$", ""))

            title = r.html.find('.product-summary__heading', first=True).text
            author = r.html.find('.product-authors', first=True).text

            return {
                "price": price,
                "name": title,
                "authors": author,
                "url": url,
                "integration": "pearson"
            }

        except AttributeError:
            return None
