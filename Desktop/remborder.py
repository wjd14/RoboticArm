from PIL import Image, ImageChops;


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((50,50)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


im = Image.open('dilatedimg2.jpg')
im = trim(im)
im.save('blahblahblah.jpg');


