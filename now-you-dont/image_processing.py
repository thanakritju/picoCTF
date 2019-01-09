from PIL import Image

img =Image.open("nowYouDont.png")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i,j]==(145, 32, 32, 255):
            pixels[i,j]=(0,0,0,255)
img.show()
