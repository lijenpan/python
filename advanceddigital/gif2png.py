"""Write a command line utility called gif2png that takes a single command line argument
(the name of a GIF file), opens the GIF file, converts the image format to PNG and
stores the converted image as a new PNG file in the current working directory.
"""

from PIL import Image
from optparse import OptionParser


def gif2png(options):
	im = Image.open(options.file_name)
	transparency = im.info['transparency'] 
	im.save('test1.png', transparency=transparency)

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="file_name", help="file name for the gif")
	options, args = parser.parse_args()
	gif2png(options)
