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
 
@app.route('/home')
def home():
    return render_template('pages/home.html');

@app.route('/moduleview')
def moduleView():
    return render_template('pages/moduleView.html');

@app.route('/lessonview')
def lessonView():
    objectivesData = load_objectives()

    return render_template('pages/lessonView.html', objectivesData=objectivesData);

# API route to provide AI chatbot functionality
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get contextual data
    user_message = request.json['message']
    objectivesData = load_objectives()

    # Send contextual data to the chatbot and get the response
    chatbot_response = chatbot_api.query(user_message, objectivesData)

    return jsonify({'response': chatbot_response})

# Main driver function
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)