import random as r
import sys
from PIL import Image, ImageFilter


def open_normal(image):
	'''show the passed image as it currently is'''
	image.show()


def change_pix(image):
	'''change a random group of pixels'''
	pixel_size = 40

	# randomly assign pixel group's location
	width, height = image.size
	start_x = r.randint(0, width-(pixel_size*2))
	start_y = r.randint(0, height-(pixel_size*2))

	# randomly generate RGB
	red = r.randint(0,255)
	green = r.randint(0,255)
	blue = r.randint(0,255)

	# set a group of pixels (TRAVERSING A GRID DEMO)
	for i in range(start_x, start_x+pixel_size):
		for j in range(start_y, start_y+pixel_size):
			image.putpixel((i,j), (red,green,blue))
	image.show()


def apply_blur(image):
	'''apply blur to the image'''
	image.filter(ImageFilter.BLUR).show()


def apply_contour(image):
	'''apply contour to the image'''
	image.filter(ImageFilter.CONTOUR).show()


def black_and_white(image):
	'''change the image to black and white'''
	width, height = image.size
	black_pixel = (0,0,0)
	white_pixel = (255,255,255)

	# loop through each pixel
	for i in range(width):
		for j in range(height):
			pixel = (i,j)
			(r,g,b) = image.getpixel(pixel)
			avg = (r+g+b) // 3

			if avg < 128:
				image.putpixel((i,j),black_pixel)
			else:
				image.putpixel((i,j),white_pixel)
	image.show()


def save(image):
	'''save the image'''
	image.save('new_'+image.filename)


def quit(*args):
	'''quit the program'''
	print('\n')	# give some space
	sys.exit()


def main():
	# validate command usage
	if len(sys.argv) != 2:
		print('Invalid usage: python3 images_stuff.py [image_path]')
	else:
		jumper = {
			'1': open_normal,
			'2': change_pix,
			'3': apply_blur,
			'4': apply_contour,
			'5': black_and_white,
			'6': save,
			'7': quit
		}

		image = Image.open(sys.argv[1])

		# save and print the height and width of the image
		width, height = image.size
		print(f'height: {height}, width: {width}')

		# get a pixel color
		print(image.getpixel((5,5)))


		while True:
			option = input('\nPlease select an option:\n  1: Open normal\n  2: Open with changed pixel group\n  3: Open with blur\n  4: Open with contour\n  5: Make black and white\n  6: Save\n  7: Quit\n\n  > ')
			
			# check to see if the command is in the jump table
			if option in jumper:
				jumper[option](image)
			else:
				print(f'\n\nInvalid option, "{option}"')


if __name__ == '__main__':
    main()