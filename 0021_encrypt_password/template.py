import os
import sys
from hashlib import sha256
from hmac import HMAC

def main(argv):
	if len(argv) != 1:
		print("Usage:template.py <password>")
		sys.exit(2)

	result = encrypt_password(argv[0])
	print("result is {}".format(result))
	salt = result[:8]
	result2 = encrypt_password(argv[0], salt)
	if result == result2:
		print("decode successfully")
	else:
		print("decode failed")

def encrypt_password(password, salt=None):
	if salt is None:
		salt = os.urandom(8)

	if isinstance(password, unicode):
		password = password.encode('UTF-8')

	result = password
	for i in xrange(10):
		result = HMAC(result, salt, sha256).hexdigest()

	return salt + result

if __name__ == '__main__':
	main(sys.argv[1:])