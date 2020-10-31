from os import listdir
import aiohttp

def get_files(directory):
    return [name for name in listdir(directory) if name[:1] != "." and name[:2] != "__" and name != "_DS_Store"]

async def request(url, json=True):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1.1.1.1.1 Safari/537.36 Edg/1.1.1.1.1"
        }) as response:
            if json:
                return await response.json()
            else:
                return await response.text()
