import aiohttp
import re

class Session:

    def __init__(self, links: bool = False):
        self.links = links

    async def upload(self, payload: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(url='https://hastebin.com/documents', data=payload.encode('utf-8')) as resp:
                key = await resp.json()
            if self.links:
                return "https://hastebin.com/" + key["key"]
            else:
                return key["key"]


    async def read(self, payload: str):
        sub = re.compile(r'(https://hastebin.com/(raw/)?)?')
        key = re.sub(sub, '', payload)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=f'https://hastebin.com/raw/{key}') as resp:
                text = await resp.text()
        await session.close()
        return text
