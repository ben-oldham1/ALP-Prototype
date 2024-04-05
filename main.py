from flask import Flask, render_template, request, jsonify
import chatbot_api
import json
 
# Flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)

# Utility functions
# Return lesson objectives loaded from file
def load_objectives():
    objectivesJson = open('static/data/lessonObjectives.json')
    objectivesData = json.load(objectivesJson)
    return objectivesData

# Return lesson content html loaded from file
def load_lesson_content():
    return 'placeholder function'
 
# Decorator which tells the application which URL should call the associated function
@app.route('/')
def index():
    return '<h1>Visit <a href="/home">/home</a> page to get started</h1>';
    
@app.route('/login')
def login():
    return render_template('pages/login.html');

@app.route('/signUp')
def signUp():
    return render_template('pages/signUp.html');
 
@app.route('/home')
def home():
    return render_template('pages/home.html');

@app.route('/moduleview')
def moduleView():
    return render_template('pages/moduleView.html');

@app.route('/account')
def account():
    return render_template('pages/account.html');

@app.route('/lessonview')
def lessonView():
    objectivesData = load_objectives()

    # Get example code
    with open('static/data/lessonCode.txt', 'r') as f:
        lessonCode = f.read()

    return render_template('pages/lessonView.html', objectivesData=objectivesData, lessonCode=str(lessonCode));

# API route to provide AI chatbot functionality
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user message
    userMessage = request.json['message']
    userCode = request.json['codeContents']

    # Get objectives for the current lesson
    objectivesData = load_objectives()

    # Get the tutorial content for current lesson
    with open('templates/tutorials/pythonLessonOne.html', 'r') as f:
        tutorialContent = f.read()

    # Send contextual data to the chatbot and get the response
    chatbot_response = chatbot_api.query(userMessage, objectivesData, userCode)

    return jsonify({'response': chatbot_response})

# Main driver function
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)