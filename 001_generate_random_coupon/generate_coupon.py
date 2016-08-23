import uuid
import sys

def main(argv):
	if len(argv) != 1:
		print("Usage:generate_coupon.py <count>")
		sys.exit(2)

	for i in range(int(argv[0])):
		print("{}:{}".format(i+1, uuid.uuid4()))



if __name__ == '__main__':
	main(sys.argv[1:])