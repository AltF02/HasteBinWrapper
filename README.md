HasteBinWrapper
===============

A asynchronous Python client for HasteBin.

Requirements
------------

- Python >= 3.7
- [aiohttp](https://docs.aiohttp.org/en/stable/)

Usage
-----

```python
import HasteBin

haste = HasteBin.Session()
```

HasteBin.Session(links=True)
Returns links

```python
haste.upload("Your text")
```
