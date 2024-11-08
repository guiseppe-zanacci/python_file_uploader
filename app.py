import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
basedir = os.path.abspath(os.path.dirname(__file__))

import setup
Setup = setup.Setup() #heh

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH= os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*60*1000)

dropzone = Dropzone(app)
@app.route(setup.route,methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'],f.filename))
    return render_template('index.html', page_title=Setup.title, page_header=Setup.header)

if __name__ == '__main__':
    if setup.serverType == "Local":
        app.run(debug=True, port=setup.port)
    elif setup.serverType == "Public":
        app.run(debug=False, port=setup.port, host='0.0.0.0')
    else:
        print("Local/Public not defined")