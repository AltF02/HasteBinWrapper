import aiohttp


class Session:

    def __init__(self, links: bool = False):
        self.links = links

    async def post_content(self, payload: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(url='https://hastebin.com/documents', data=payload.encode('utf-8')) as resp:
                key = await resp.json()
                if self.links:
                    return "https://hastebin.com/" + key["key"]
                else:
                    return key["key"]
