from flask import Flask, render_template, request
import uuid, os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'tmp'

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        new_filename = uuid.uuid1()
        _, ext = os.path.splitext(f.filename)
        f.save('uploaded/%s%s' % (new_filename, ext))
        return "file uploaded successfully : )"
    return render_template('upload.html')
    
if __name__ == '__main__':
   app.run(debug = True)