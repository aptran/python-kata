# scraper using multiprocessing
from multiprocessing import Pool, Queue
import requests
import re
from datetime import datetime
import sys

def make_request(url):
	response = requests.get(url)
	html = response.text

	title = re.search('<title>(.+?)</title>', html)
	if title:
		m = title.group(1)
		return m
	else:
		return 'No title.'


def without_processes(request_count, url):
	print('Beginning %d requests without processes...' % request_count)
	start_time = datetime.now()
	for i in range(request_count):
		make_request(url)

	end_time = datetime.now()
	print('Without processes:', (end_time - start_time).total_seconds())



def work(url):
	make_request(url)


def with_processes(request_count, url):
	pool_count = 5
	print('Beginning requests %d with %d processes...' % (request_count, pool_count))
	start_time = datetime.now()

	q = Queue()
	pool = Pool(pool_count)

	tasks = [url for i in range(request_count)]
	results = pool.map(work, tasks)

	pool.close()
	pool.join()

	end_time = datetime.now()
	print('With processes:', (end_time - start_time).total_seconds())


if __name__ == '__main__':
	url = 'http://en.wikipedia.org/wiki/Special:Random'
	request_count = 100

	if len(sys.argv) > 1:
		url = sys.argv[1]

	if len(sys.argv) > 2:
		request_count = int(sys.argv[2])

	without_processes(request_count, url)
	print('')
	with_processes(request_count, url)

