import aiohttp
import json
import asyncio


class HasteBin:

    def __init__(self, links: bool = False):
        self.links = links

    async def post_content(self, payload: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(url='https://hastebin.com/documents', data=payload) as resp:
                key = json.loads(await resp.text())
                if self.links:
                    return "https://hastebin.com/" + key["key"]
                else:
                    return key["key"]
                    
                    
