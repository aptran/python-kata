# scraper using multiprocessing
from multiprocessing import Process
import requests
import re
from datetime import datetime

def make_request():
	#response = requests.get('http://en.wikipedia.org/wiki/Special:Random')
	response = requests.get('http://justinyan.com')
	html = response.text

	title = re.search('<title>(.+?)</title>', html)
	if title:
		m = title.group(1)
		print m
	else:
		print 'No title.'
	return


def without_processes():
	print 'Beginning requests without processes...'
	start_time = datetime.now()
	for i in range(5):
		make_request()
	end_time = datetime.now()
	print 'Without processes:', end_time - start_time


def with_processes():
	print 'Beginning requests with processes...'
	start_time = datetime.now()
	jobs = []
	for i in range(5):
		p = Process(target=make_request)
		jobs.append(p)
		p.start()

	for j in jobs:
		j.join()

	end_time = datetime.now()
	print 'With processes:', end_time - start_time


if __name__ == '__main__':
	with_processes()
	print '\n'
	without_processes()

