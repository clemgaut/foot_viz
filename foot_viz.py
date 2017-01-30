import os
from flask import Flask, request, redirect, flash, render_template, jsonify
import jinja2

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        json_data = request.files['file'].read()
        if json_data == '':
            flash('No selected file')
            return redirect(request.url)
        print(json_data)
        return render_template('visu.html', data=eval(json_data))
    return '''
    <!doctype html>
    <title>Upload football data( .json)</title>
    <h1>Upload football data( .json)</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run()
