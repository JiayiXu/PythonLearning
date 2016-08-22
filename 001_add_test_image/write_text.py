from PIL import Image, ImageFont, ImageDraw
import sys, getopt

def main(argv):
	file_name = ''
	text = ''
	try:
		opts, args = getopt.getopt(argv, "hf:t:", ["filename=", "text="])
	except getopt.GetoptError:
		print "write_text.py -f <filename> -t <text>"
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print "write_text.py -f <filename> -t <text>"
			sys.exit(0)
		elif opt in ("-f", "--filename"):
			file_name = arg
		elif opt in ("-t", "--text"):
			text = arg

	img = Image.open(file_name)
	draw = ImageDraw.Draw(img)
	fontsize = 1
	img_fraction = 0.3
	font = ImageFont.truetype('/Library/Fonts/Arial.ttf', fontsize)
	while font.getsize(text)[0] < img_fraction*img.size[0]:
	    # iterate until the text size is just larger than the criteria
	    fontsize += 1
	    font = ImageFont.truetype("/Library/Fonts/Arial.ttf", fontsize)

	fontsize -= 1
	font = ImageFont.truetype("/Library/Fonts/Arial.ttf", fontsize)
	font_size = font.getsize(text)
	image_size = img.size

	text_start_position = (image_size[0] - font_size[0], font_size[1])
	draw.text(text_start_position, "text", font=font, fill=(255,0,0,128))
	img.show()

if __name__ == '__main__':
	main(sys.argv[1:])