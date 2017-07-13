from flask import jsonify
from flask import render_template
from flask import request

from mosaic import app
from .utils.image_2_mosaic import create_mosaic
from .utils.utils import image_to_string, allowed_file


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify(message='No file part')
        file = request.files['file']
        if file.filename == '':
            return jsonify(message='No selected file')
        if file and allowed_file(file.filename):
            image = create_mosaic(file, app.config['COLOR_MAP'])
            base64_image = image_to_string(image)
            return jsonify(result="data:image/png;base64, %s" % base64_image)
        else:
            return jsonify(message='file extension not allowed')
    else:
        return render_template('index.html',
                               title='Upload')

