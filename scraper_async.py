import asyncio
import aiohttp
import re
from datetime import datetime
import requests


'''
Synchronous requests

'''
def fetch_sync(count):
    responses = []
    start_time = datetime.now()
    for i in range(count):
        responses.append(requests.get('https://en.wikipedia.org/wiki/Special:Random').text)
    end_time = datetime.now()
    total_time = end_time - start_time

    print('Sync time taken in (s): ', total_time.total_seconds())

    print_responses(responses)



'''
Asynchronous requests

'''
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def run(loop,  r):
    url = "https://en.wikipedia.org/wiki/Special:Random"
    tasks = []
    start_time = datetime.now()
    for i in range(r):
        task = asyncio.ensure_future(fetch(url))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    end_time = datetime.now()
    total_time = end_time - start_time

    print('Async time taken in (s): ', total_time.total_seconds())
    print_responses(responses)

def print_responses(responses):
    for r in responses:
        title = re.search('<title>(.*)</title>', r).group(1)

        print(title)


'''
Run time comparison 
'''
fetch_sync(5)
print('\n')

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, 5))
loop.run_until_complete(future)

