# Image Resizer - file1

from PIL import Image

img_path = input("Enter image path: ")
img = Image.open(img_path)

new_width = int(input("New width: "))
new_height = int(input("New height: "))

resized = img.resize((new_width, new_height))
resized.save("resized_image.jpg")

print("Image resized successfully!")
