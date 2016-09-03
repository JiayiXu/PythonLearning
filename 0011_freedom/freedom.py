import uuid
import sys
import codecs

def main(argv):
	if len(argv) != 1:
		print("Usage:freedom.py words.txt")
		sys.exit(2)

	filters = generate_filters(argv[0])

	while True:
		name = raw_input('please input: ').decode('utf-8')
		for filter in filters:
			name = name.replace(filter, '*' * len(filter))

		print(name)

def generate_filters(path):
	filters = []
	with codecs.open(path, encoding='utf-8') as ins:
		for line in ins:
			word = line.strip()
			filters.append(word)

	return filters

if __name__ == '__main__':
	main(sys.argv[1:])