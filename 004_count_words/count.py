import operator
import sys

def main(argv):
	if len(argv) < 1:
		print("Usage:get_count.py <file> <top count=10>")
		sys.exit(2)

	file_name = argv[0]
	top_count = 10
	if len(argv) > 1:
		top_count = int(argv[1])

	word_count = {}
	with open(file_name, 'r') as file:
		for line in file:
			splits = line.split(' ')
			for word in splits:
				if word not in word_count:
					word_count[word] = 0
				
				word_count[word] = word_count[word] + 1

	sorted_x = sorted(word_count.items(), key=operator.itemgetter(1))
	sorted_x.reverse()
	top_k = sorted_x[:top_count]
	print("top k is {}".format(top_k))

if __name__ == '__main__':
	main(sys.argv[1:])