HasteBinWrapper
===============

A asynchronous Python client for HasteBin.

Requirements
------------

- Python >= 3.7
- [aiohttp](https://docs.aiohttp.org/en/stable/)

Installation
------------
```
pip install git+https://github.com/DankDumpster/HasteBinWrapper
```


Usage
-----

```python
import hastebin

haste = hastebin.Session()
```

hastebin.Session(links=True)
Returns links

```python
link = await haste.upload("Your text")
```

```python
content = await haste.read("HasteBin Link")
```

Example
-------
```python
import haste
import asyncio

haste = haste.Session(links=True)  # initiates the client


async def main():
    link = await haste.upload(payload="import random\n"
                                      "print(random.randint(0, 5))")  # Sends the code to the wrapper and uploads it to HasteBin, and returns the link where its stored
    content = await haste.read(payload=link)  # Gets the data from the link
    print(content)  # Prints import random\n print(random.randint(0, 5))


asyncio.get_event_loop().run_until_complete(main())
```
