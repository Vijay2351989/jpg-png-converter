import os
import sys
from PIL import Image

source = sys.argv[1]
print(source)

dest = sys.argv[2]
print(dest)

if(not os.path.isdir(source)):
    print('Source directory does not exist')
else:
    if(not os.path.isdir(dest)):
        os.mkdir(dest)
    for file in os.listdir(source):
        if(file.endswith(".jpg")):
            img = Image.open(f'./{source}/{file}')
            img.save(f'./{dest}/{file.split(".")[0]}.png', "png")
