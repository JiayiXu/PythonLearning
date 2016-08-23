import uuid
import sys
import sqlite3

def main(argv):
	if len(argv) != 1:
		print("Usage:generate_coupon.py <count>")
		sys.exit(2)

	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('DELETE FROM Coupons')
	conn.commit()
	coupons = [(i+1, str(uuid.uuid4()))
			   for i in range(int(argv[0]))
			  ]
	c.executemany('INSERT INTO Coupons VALUES (?,?)', coupons)
	c.execute('SELECT * FROM Coupons')
	print(c.fetchall())


if __name__ == '__main__':
	main(sys.argv[1:])