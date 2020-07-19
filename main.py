from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from logic import find_text

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

app = Flask(__name__)


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      try:
         f = request.files['file']
      except:
         return render_template("display.html", msg="No file selected")
      
      
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


@app.route('/')
def index():
	return render_template("upload.html")


if __name__ == "__main__":
	app.run(debug=True)