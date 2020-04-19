import aiohttp


class Session:

    def __init__(self, links: bool = False):
        self.links = links
        self.session = aiohttp.ClientSession()

    async def upload(self, payload: str):
        async with self.session.post(url='https://hastebin.com/documents', data=payload.encode('utf-8')) as resp:
            key = await resp.json()
            if self.links:
                return "https://hastebin.com/" + key["key"]
            else:
                return key["key"]

    async def read(self, payload: str):
        async with self.session.get(url=payload) as resp:
            return resp.text()
