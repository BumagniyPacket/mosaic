import os
from PIL import Image

from mosaic import app

IMG_DIR = '../../img/'

# image max size
MAX_SIZE = 2048
#
FRAGMENTS_COUNT = 50
FRAGMENT_SHAPE = 60


def fill_color_map_pil(fragment_dir):
    tmp = dict()
    for fragment_name in os.listdir(fragment_dir):
        if fragment_name.startswith('.'):
            continue
        color = fragment_name.split('.')[0]
        img = Image.open(os.path.join(fragment_dir, fragment_name)).convert('L')
        fragment = img.resize([FRAGMENT_SHAPE] * 2)
        tmp[int(color)] = fragment
    return tmp


def _get_image_by_color(color):
    if color not in app.config['COLOR_MAP'].keys():
        return _get_image_by_color(color + 1)
    else:
        return app.config['COLOR_MAP'][color]


def make_great_mosaic_again_pil(image_path):
    # open image
    image = Image.open(image_path).convert('L')
    # grep image size
    w, h = image.size

    # check image width. if width < FRAGMENT_SHAPE then resize to fragment width
    if w < FRAGMENT_SHAPE:
        scale = FRAGMENT_SHAPE / w
        image = image.resize([w * scale, h * scale])
        h, w = image.size

    # calculate blank image width an height
    blank_w = FRAGMENTS_COUNT
    blank_h = int(blank_w * (h / w))

    # create blank image
    blank = Image.new('L', [blank_w * FRAGMENT_SHAPE,
                            blank_h * FRAGMENT_SHAPE])
    # calculate color pick fragment
    step = int(w / FRAGMENTS_COUNT)

    # picking color and put to blank image fragment with needed color
    for i in range(0, blank_h):
        for j in range(0, blank_w):
            fragment_color = image.getpixel((j * step, i * step))
            color_image = _get_image_by_color(int(fragment_color))

            x = j * FRAGMENT_SHAPE
            y = i * FRAGMENT_SHAPE

            # blank[y:y + FRAGMENT_SHAPE, x:x + FRAGMENT_SHAPE] = color_image
            blank.paste(color_image, (x, y))

    return blank


if __name__ == '__main__':
    img_path = '../../cat.jpg'

    # app.config['COLOR_MAP'] = fill_color_map(IMG_DIR)
    app.config['COLOR_MAP'] = fill_color_map_pil(IMG_DIR)

    # make_great_mosaic_again(img_path)
    make_great_mosaic_again_pil(img_path)
