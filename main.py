from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from logic import find_text, change_to_png
from flask.cache import Cache

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

cache = Cache(app,config={'CACHE_TYPE': 'simple'})
app = Flask(__name__)
cache.init_app(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@cache.cached(timeout=50)
@app.route('/')
def index():
	return render_template("upload.html", msg=False)
   
@cache.cached(timeout=50)
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
         try:
            files = flask.request.files.getlist("file").filenames
         except:
            return render_template('upload.html', msg='No file was selected')

         # if files and allowed_file(files.filename):
         print("AAAAAAAAAAa")

         texts = find_text(files)
         print(texts)

         return render_template('display.html',
                              text=texts,
                              file_name=files.filename)
   return render_template('upload.html', msg=False)





if __name__ == "__main__":
	app.run(debug=True)