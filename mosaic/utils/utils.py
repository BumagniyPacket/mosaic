import base64
from io import BytesIO

from mosaic import app


def image_to_string(image):
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)
    base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return base64_image


def allowed_file(filename):
    return '.' in filename and \
           filename.lower().rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
