from PIL import Image
import os

folder = "images"
for file in os.listdir(folder):
    if file.endswith(".jpg"):
        path = os.path.join(folder, file)
        img = Image.open(path)
        img.save(path, "JPEG", quality=80, optimize=True, progressive=True)
