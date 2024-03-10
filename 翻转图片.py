from PIL import Image

img = Image.open('misc55.png')

img.transpose(Image.FLIP_TOP_BOTTOM).save('out.png')