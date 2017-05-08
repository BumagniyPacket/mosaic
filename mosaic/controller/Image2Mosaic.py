import os
from PIL import Image

FRAGMENT_SHAPE = 30
MINIMAL_SHAPE = FRAGMENT_SHAPE * 3


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

    if normal_image_w < normal_image_h:
        w_fragments = fragments_count
        h_fragments = int(w_fragments * (normal_image_h / normal_image_w))
    else:
        h_fragments = fragments_count
        w_fragments = int(h_fragments * (normal_image_w / normal_image_h))

    step = normal_image_w // fragments_count

    blank_w = w_fragments * FRAGMENT_SHAPE
    blank_h = h_fragments * FRAGMENT_SHAPE

    blank = Image.new('L', [blank_w, blank_h])

    for i in range(0, h_fragments):
        for j in range(0, w_fragments):
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
    save(img)
