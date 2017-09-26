# We create a class with some attributes
class Image:

    def __init__(self):
        self.ext = ''
        self.size = ''
        self.data = ''


# Create an instance of the Image class
img = Image()
img.ext = 'bmp'
img.size = '8'
img.data = [255, 255, 255, 200, 34, 35]

# We add this new attribute dynamically
img.ids = 20

print(img.ext, img.size, img.data, img.ids)
