import uuid
import sys
import os

def main(argv):
	if len(argv) != 1:
		print("Usage:count_count_info.py <path>")
		sys.exit(2)

	count_code = 0
	count_comments = 0
	count_spaces = 0
	for dirpath, _, filenames in os.walk(argv[0]):
		for file_name in filenames:
			if os.path.splitext(file_name)[1] == '.py':
				full_path = os.path.join(dirpath, file_name)
				code, comments, spaces = get_statistics(full_path)
				count_code += code
				count_comments += comments
				count_spaces += spaces

	print("Count_code:%s, count_comments:%s, count_spaces:%s" % (count_code, count_comments, count_spaces))

def get_statistics(full_path):
	count_code = 0
	count_comments = 0
	count_spaces = 0
	with open(full_path, "r") as ins:
		is_start_of_comments = False
		for line in ins:
			context = line.strip()
			if context.startswith('#') or context.startswith('"""') or is_start_of_comments is True:
				count_comments += 1
			elif context == '':
				count_spaces += 1
			else:
				count_code += 1

			if context.startswith('"""'):
				is_start_of_comments = True
			
			if context[::-1].startswith('"""'):
				is_start_of_comments = False

	return count_code, count_comments, count_spaces

if __name__ == '__main__':
	main(sys.argv[1:])