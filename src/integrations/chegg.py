from requests_html import HTMLSession


class Chegg:
    def __init__(self):
        pass

    async def search(self, isbn):
        session = HTMLSession()
        url = f"https://www.campusbooks.com/search/{isbn}?buysellrent=buy.html"
        r = session.get(url)

        title = r.html.find('h1.page-header', first=True).text
        vendors = r.html.find('tr')
        authors = r.html.find('dt')

        writer = ""
        price = ""

        for author in authors:
            auth = author.find('strong', first=True)

            if auth and auth.text == "Authors":
                writer = author.text.replace("Authors: ", "")
                break

        for vendor in vendors:
            tag = vendor.find('[title~=Chegg]', first=True)

            if tag:
                price = vendor.find('td .price', first=True).text

                if not price or isinstance(price, int):
                    return None

                break

        try:
            price = float(price.replace("$", ""))
        except ValueError:
            return None

        return {
            "price": price,
            "url": url,
            "name": title,
            "authors": writer,
            "integration": "chegg"
        }
