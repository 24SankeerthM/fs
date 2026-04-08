STEP 1 — Create GitHub Repository and Folders
1.	Open GitHub → New Repository 
2.	Name: web-app-engine 
Create files and folders using Add file → Create new file
Create this structure:
Web_app/
   app.yaml
   main.py
   requirements.txt
   templates/
       index.html
-	Paste the code (given below) into respective files and Commit.
STEP 2 — Open Google Cloud Console
1.	Go to: https://console.cloud.google.com 
2.	Create New Project 
3.	Enable It.
STEP 3 — Enable App Engine Admin API
1.	≡ Menu → APIs & Services → Library 
2.	Search App Engine Admin API 
3.	Click Enable 
4.	If asked → Authorize
STEP 4 — Open Cloud Shell (Shield / Square Icon)
Look at top-right corner
You will see:
[ >_ ]
First time:
•	Click Authorize / Enable 
•	Wait for terminal to start 
Then click:
Open Editor
STEP 5 — Create App Engine using command
In terminal:
gcloud app create
-	Select region
-	App Engine is created
STEP 6 — Clone GitHub Project
git clone https://github.com/your-username/web-app-engine.git
cd web-app-engine/Web_app
STEP 7 — Run Project
python main.py
STEP 8 — View Web Page
Click:
Web Preview 🌐 → Preview on port 8080
Output:
Success! Your Python-powered HTML is running.	
STEP 9 — Stop Server
fuser -k 8080/tcp
STEP 10 — Deploy to App Engine
gcloud app deploy
Press Y
Then:
gcloud app browse




CODE to be used
app.yaml
runtime: python39
entrypoint: gunicorn -b :$PORT main:app

main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

requirements.txt
flask==3.0.0
gunicorn==21.2.0

templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Success! Your Python-powered HTML is running.</h1>
</body>
</html>
...
Web_app ->folder
app.yaml
main.py
requirements.txt
templates ->folder
index.html


app.yaml
runtime: python39

# GAE looks for an 'app' object in main.py to start the server
entrypoint: gunicorn -b :$PORT main:app

main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # render_template automatically looks in the /templates folder
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    # Local development server
    app.run(host='127.0.0.1', port=8080, debug=True)

reqirements.txt
flask==3.0.0
gunicorn==21.2.0
Index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f4f4f9; }
        .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
        h1 { color: #4285F4; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Success!</h1>
        <p>Your Python-powered HTML is running.</p>
    </div>
</body>
</html>


Command to kill : fuser -k 8080/tcp
