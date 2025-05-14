from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

client = MongoClient("mongodb://localhost:27017/")
db = client['code_collab']
teams = db.teams
messages = db.messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_team', methods=['POST'])
def create_team():
    projectName = request.form['projectName']
    usns = request.form.getlist('usns')
    usns = [u.strip() for u in usns if u.strip()]
    if len(usns) < 4:
        return "At least 4 members required"
    teams.insert_one({'projectName': projectName, 'members': usns})
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    projectName = request.form['projectName']
    usn = request.form['usn']
    team = teams.find_one({'projectName': projectName, 'members': usn})
    if not team:
        return "Invalid login"
    msgs = list(messages.find({'projectName': projectName}))
    return render_template('dashboard.html', usn=usn, projectName=projectName, messages=msgs)

@app.route('/send_message', methods=['POST'])
def send_message():
    usn = request.form['usn']
    projectName = request.form['projectName']
    message = request.form.get('message', '').strip()
    file = request.files.get('codefile')

    filename = ""
    code_content = message

    if file and file.filename:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        with open(filepath, 'r') as f:
            code_content = f.read()

    messages.insert_one({
        'sender': usn,
        'projectName': projectName,
        'filename': filename if filename else '(message only)',
        'code': code_content
    })

    return redirect(url_for('login'), code=307)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
