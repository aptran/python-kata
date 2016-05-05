import asyncio
import aiohttp
import re
from datetime import datetime
import requests
import sys

'''
Synchronous requests

'''
def fetch_sync(count, url):
    responses = []
    start_time = datetime.now()
    for i in range(count):
        responses.append(requests.get(url).text)
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

async def run(loop, r, url):
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



'''
Find <title> and print
'''

def print_responses(responses):
    for r in responses:
        title = re.search('<title>(.*)</title>', r)
        if title:
            print(title.group(1))
        else:
            print('No title found.')


'''
Run time comparison 
'''
url = "https://en.wikipedia.org/wiki/Special:Random"
num_loops = 5

if len(sys.argv) > 1:
    url = sys.argv[1]

if len(sys.argv) > 2:
    num_loops = int(sys.argv[2])

fetch_sync(num_loops, url)
print('\n')

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, num_loops, url))
loop.run_until_complete(future)

