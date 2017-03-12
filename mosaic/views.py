import base64
from flask import jsonify
from flask import render_template
from flask import request
from io import BytesIO

from mosaic import app
from .controller.Image2Mosaic import create_mosaic


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    def allowed_file(filename):
        return '.' in filename and \
               filename.lower().rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify(message='No file part')

        file = request.files['file']
        if file.filename == '':
            return jsonify(message='No selected file')

        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            image = create_mosaic(file, app.config['COLOR_MAP'])

            buffer = BytesIO()
            image.save(buffer, format='JPEG')
            buffer.seek(0)
            base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

            return jsonify(result="data:image/png;base64, %s" % base64_image)

        else:
            return jsonify(message='file extension not allowed')

    else:
        return render_template('index.html',
                               title='Upload')
