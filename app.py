import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
import hashlib
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

import setup
Setup = setup.Setup() #heh

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH= os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*60*1000,
    QUARANTINE_PATH = os.path.join(basedir,'quarantine'))

dropzone = Dropzone(app)
@app.route(setup.route,methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        if f.filename.endswith(('.exe', '.dll', '.sh')):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            content_hash = hashlib.sha256(f.read()).hexdigest()
            f.seek(0)

            original_filename = f.filename
            encoded_filename = original_filename.replace('/', '(slash)').replace('\\', '(backslash)', ' ', '(space)')
            safe_filename = f"{timestamp}_{encoded_filename}_{content_hash[:8]}"        
            
            filepath = os.path.join(['QUARANTINE_PATH'], safe_filename)

            if not filepath.startswith(os.path.abspath(['QUARANTINE_PATH'])):
                raise Exception("Path traversal not good")
            else:
                f.save(filepath)
                os.chmod(filepath, 0o600)
        else:
            f.save(os.path.join(app.config['UPLOADED_PATH'],f.filename))
    return render_template('index.html', page_title=Setup.title, page_header=Setup.header)

if __name__ == '__main__':
    if setup.serverType == "Local":
        app.run(debug=True, port=setup.port)
    elif setup.serverType == "Public":
        app.run(debug=False, port=setup.port, host='0.0.0.0')
    else:
        print("Local/Public not defined")