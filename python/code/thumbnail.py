from PIL import Image

size = (128, 128)
saved = "africa.jpg"

im =  Image.open("africa.tif")
im.thumbnail(size)
im.save(saved)
im.show()
