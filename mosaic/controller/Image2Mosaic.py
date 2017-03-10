import os
from PIL import Image

FRAGMENT_SHAPE = 30


def fill_color_map(fragment_dir):
    # init data base of fragments
    tmp = dict()
    for fragment_name in os.listdir(fragment_dir):
        if fragment_name.startswith('.'):
            continue
        color = fragment_name.split('.')[0]
        fragment_path = os.path.join(fragment_dir, fragment_name)
        img = Image.open(fragment_path).convert('L')
        fragment = img.resize([FRAGMENT_SHAPE] * 2)
        tmp[int(color)] = fragment
    return tmp


def create_mosaic(image_path, color_map, fragments_count=60):
    """

    :param image_path:
    :param fragments_count:
    :param color_map:
    :return:
    """

    def get_image_by_color(color):
        if color not in color_map.keys():
            return get_image_by_color(color + 1)
        else:
            return color_map[color]

    # open image
    image = Image.open(image_path).convert('L')
    # grep image size
    w, h = image.size
    # check image width. if width < FRAGMENT_SHAPE then resize
    # to fragment width
    if w < FRAGMENT_SHAPE:
        scale = FRAGMENT_SHAPE / w
        image = image.resize([w * scale, h * scale])
        w, h = image.size
    # calculate blank image width an height
    blank_w = fragments_count
    blank_h = int(blank_w * (h / w))
    # create blank image
    blank = Image.new('L', [blank_w * FRAGMENT_SHAPE,
                            blank_h * FRAGMENT_SHAPE])
    # calculate color pick fragment
    step = int(w / fragments_count)
    # picking color and put to blank image fragment with needed color
    for i in range(0, blank_h):
        for j in range(0, blank_w):
            fragment_color = image.getpixel((j * step, i * step))
            color_image = get_image_by_color(int(fragment_color))
            blank.paste(color_image, (j * FRAGMENT_SHAPE, i * FRAGMENT_SHAPE))
    return blank


if __name__ == '__main__':
    img_path = '../../cat.jpg'
    colormap = fill_color_map('../../img')
    # make_great_mosaic_again(img_path)
    mosaic = create_mosaic(img_path, colormap, 60)
    # mosaic.show()
    mosaic.save('ret.jpg')
