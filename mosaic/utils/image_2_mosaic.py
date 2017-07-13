import os
from PIL import Image

FRAGMENT_SHAPE = 30
MINIMAL_SHAPE = FRAGMENT_SHAPE * 6


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


def normalize_image(image):
    w, h = image.size

    if min(w, h) < MINIMAL_SHAPE:
        scale = MINIMAL_SHAPE / min(w, h)
        return image.resize([int(w * scale), int(h * scale)])
    else:
        return image


def create_mosaic(image_path, color_map, fragments_count=60):
    def get_image_by_color(color):
        if color not in color_map.keys():
            return get_image_by_color(color + 1)
        else:
            return color_map[color]

    image = Image.open(image_path).convert('L')
    normal_image = normalize_image(image)
    normal_image_w, normal_image_h = normal_image.size

    # TODO:????
    if normal_image_w < normal_image_h:
        frag_count_w = fragments_count
        frag_count_h = int(frag_count_w * (normal_image_h / normal_image_w))
        step = normal_image_w // fragments_count
    else:
        frag_count_h = fragments_count
        frag_count_w = int(frag_count_h * (normal_image_w / normal_image_h))
        step = normal_image_h // fragments_count

    blank_w = frag_count_w * FRAGMENT_SHAPE
    blank_h = frag_count_h * FRAGMENT_SHAPE

    blank = Image.new('L', [blank_w, blank_h])

    for i in range(0, frag_count_h):
        for j in range(0, frag_count_w):
            fragment_color = normal_image.getpixel((j * step, i * step))
            color_image = get_image_by_color(int(fragment_color))

            blank.paste(color_image, (j * FRAGMENT_SHAPE, i * FRAGMENT_SHAPE))
    return blank


if __name__ == '__main__':
    img_path = 'test/cat.png'
    # img_path = 'test/cat_tall.png'
    img_path = 'test/cat_small.png'
    colormap = fill_color_map('../../img')

    img = create_mosaic(img_path, colormap)
