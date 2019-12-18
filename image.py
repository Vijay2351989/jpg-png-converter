from PIL import Image, ImageFilter, PSDraw

img = Image.open('./images/astro.jpg')

print(img.size)

#new_image = img.resize((400, 400))
# new_image.save('thumbnail.jpg')

img.thumbnail((400, 400))
img.save('thumbnail.jpg')
