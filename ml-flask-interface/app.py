from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

from mlinterface import get_category
import os
UPLOAD_FOLDER = './static/img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET', 'POST'])
def broken():
    if request.method == 'POST':
        image = request.files['file']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_category = get_category(image.filename)

        return render_template('result.html', category=image_category)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)