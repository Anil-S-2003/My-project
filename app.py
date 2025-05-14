from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
import logging

# Logging for debug
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# MongoDB connection from environment variable
mongo_url = os.environ.get("MONGO_URI")  # Remove default for production
if not mongo_url:
    raise ValueError("MONGO_URI environment variable is not set.")
client = MongoClient(mongo_url)
db = client['code_collab']
teams = db.teams
messages = db.messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_team', methods=['POST'])
def create_team():
    try:
        projectName = request.form['projectName']
        usns = request.form.getlist('usns')
        usns = [u.strip() for u in usns if u.strip()]
        if len(usns) < 4:
            return "At least 4 members required"
        teams.insert_one({'projectName': projectName, 'members': usns})
        return redirect('/')
    except Exception as e:
        logging.exception("Error in /create_team")
        return f"Error: {str(e)}", 500

@app.route('/login', methods=['POST'])
def login():
    try:
        projectName = request.form['projectName']
        usn = request.form['usn']
        team = teams.find_one({'projectName': projectName, 'members': usn})
        if not team:
            return "Invalid login"
        msgs = list(messages.find({'projectName': projectName}))
        return render_template('dashboard.html', usn=usn, projectName=projectName, messages=msgs)
    except Exception as e:
        logging.exception("Error in /login")
        return f"Login failed: {str(e)}", 500

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
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

        return redirect(url_for('login'))  # Redirect to login, but it's usually a GET route.
    except Exception as e:
        logging.exception("Error in /send_message")
        return f"Message failed: {str(e)}", 500

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)  # Ensure uploads folder exists
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
