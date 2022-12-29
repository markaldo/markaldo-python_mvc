from fileinput import filename
from itertools import count
from flask import Flask, session,render_template, redirect, url_for, request, make_response
import uuid, os

app = Flask(__name__)
app.secret_key = 'kvpg_YbdT2d45'
app.config['UPLOAD_FOLDER'] = 'class5/tmp'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template(
            'upload.html',
            username=username
            )
    return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    id  = request.form['title']
    f = request.files['file']

    if request.form['submit'] == 'add':
        if id == "":
            return "Please enter memory title!"
        if f is None:
            return "No file attached, please upload a file!"
        if id is not None and f is not None:
            new_filename = uuid.uuid1()
            _, ext = os.path.splitext(f.filename)
            f.save('class5/static/uploads/%s%s' % (new_filename, ext))
            session[id] =  str(new_filename)+ext
            msg = "file uploaded successfully : )"
        return render_template("upload.html",
                                msg = msg
                                )
        
    if request.form['submit'] == 'display':
        return display()

def display(): 
    memo = session.copy()
    memo.pop("username")
    reply = 2 
    return render_template("final.html",
                           reply = reply,
                           memo = memo)

@app.route('/remove',  methods=['GET', 'POST'])
def remove():
        dl = request.form['remove']
        session.pop(dl, None)
        reply = 4
        return render_template("upload.html", reply = reply, dl = dl)
    
@app.route('/edit')
def edit():
   return render_template('upload.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug = True)

   