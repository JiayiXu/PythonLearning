import requests
import re
from HTMLParser import HTMLParser
import sys
import time
import os
from concurrent import futures


class Mode(object):
	SEQ = 1
	FUTURE = 2

def main(argv):
	if len(argv) != 2:
		print("Usage:.py <count> <seq|future>")
		sys.exit(2)

	url = argv[0]

	mode = None
	if argv[1] == 'seq':
		mode = Mode.SEQ
	elif argv[1] == 'future':
		mode = Mode.FUTURE
	else:
		assert "Mode has to be defined"

	res = requests.get(url)
	parser = ImgHtmlParser()
	start = time.time()
	parser.feed(res.content.decode('utf-8'))
	print("Done parsing the page: {}".format(time.time() - start))

	start = time.time()
	if mode == Mode.SEQ:
		for i in range(len(parser.imgs)):
			process_one(parser.imgs[i], 'Image_%s.jpg' % i)
		print("Seq: Done saving: {}".format(time.time() - start))
	elif mode == Mode.FUTURE:
		MAX_WORKERS = 2
		workers = min(MAX_WORKERS, len(parser.imgs))
		with futures.ThreadPoolExecutor(workers) as executor:
			future = []
			for i in range(len(parser.imgs)):
				future.append(executor.submit(process_one, parser.imgs[i], 'Image_%s.jpg' % i))

			for f in futures.as_completed(future):
				res = f.result()
				print("future:{} is {}".format(f, res))

		print("Future: Done saving: {}".format(time.time() - start))

def process_one(url, file_name):
	save_image(download_image(url), file_name)

def download_image(url):
	return requests.get(url).content

def save_image(image, file_name):
	dest_path = os.path.join('destination', file_name)
	if not os.path.exists(os.path.dirname(dest_path)):
		try:
			os.makedirs(os.path.dirname(dest_path))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise
	with open(dest_path, 'wb') as fp:
		fp.write(image)

class ImgHtmlParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.imgs = []

	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			image = [value for name, value in attrs if name == 'src']
			assert len(image) == 1
			if should_include(image[0]):
				#print("Getting %s" % image[0])
				self.imgs.append(image[0])


def should_include(url):
	if url.find('imgsrc.baidu.com') > 0 and url.find('/pic/item') < 0:
		return True
	else:
		return False

if __name__ == '__main__':
	main(sys.argv[1:])